import os
import re
from pathlib import Path

import convertapi

from .Exeptions import (
    CantConvertImageError,
    NotSupportedFormatError,
)


class Avatar:
    input_format_images = (
        "bmp",
        "fax",
        "heic",
        "ico",
        "images",
        "jpeg",
        "jpg",
        "mdi",
        "png",
        "psd",
        "svg",
        "tif",
        "tiff",
        "webp",
    )

    def path_to_save(self, name_image: str, **kwargs) -> Path:
        try:
            user_id = self.id
        except AttributeError:
            user_id = kwargs.get("id")

        path = Path(os.path.join("avatar", str(user_id), name_image))
        format_image = re.search(r"^.([a-z]*)", path.suffix).group(1)

        try:
            if Avatar.input_format_images.index(format_image):
                return path
        except ValueError:
            raise NotSupportedFormatError("Not supported this format image")

    def convert_image(self, request, path_image: str, user_id: int) -> Path:
        convertapi.api_secret = os.getenv("API_SECRET")

        format_image = re.search(r"\.([a-z]*)", path_image).group(1)

        dir_image = os.path.join("media", "avatar", str(user_id))
        output_image_name = f"{request.user}_id={user_id}_number_image={len(os.listdir(dir_image))}"

        try:
            result = convertapi.convert(
                "webp",
                {"File": path_image, "FileName": output_image_name},
                from_format=format_image,
            )
            result.save_files(dir_image)
        except convertapi.ApiError:
            raise CantConvertImageError("Can`t to convert image")

        path_to_output_image = Path(
            os.path.join(
                "avatar", str(user_id), result.response["Files"][0]["FileName"]
            )
        )

        return path_to_output_image

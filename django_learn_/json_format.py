from datetime import datetime


from pythonjsonlogger import jsonlogger


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)

        if not log_record.get("timestamp"):
            log_record["timestamp"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

        if log_record.get("level"):
            log_record["level"] = log_record["level"].upper()
        else:
            log_record["level"] = record.levelname


formatter = CustomJsonFormatter("%(timestamp)s %(level)s %(name)s %(message)s")

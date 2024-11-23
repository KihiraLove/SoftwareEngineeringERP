from datetime import datetime
from Entries.Bases.WarehouseTaskBase import WarehouseTaskBase
from Utils import Config


class WarehouseTask(WarehouseTaskBase):
    # Don't forget to document this
    def __init__(self, id: int, date: datetime, status: str, sales_order_id: int, user_id: int) -> None:
        super().__init__(id, date, status)
        self.sales_order_id = sales_order_id
        self.user_id = user_id
        return

    def __repr__(self):
        return (f"{{"
                f"\"id\": \"{self.id}\","
                f"\"date\": \"{self.date.strftime(Config.TIME_FORMAT)}\","
                f"\"status\": \"{self.status}\","
                f"\"sales_order_id\": \"{self.sales_order_id}\","
                f"\"user_id\": \"{self.user_id}\""
                f"}}")

    def get_id(self) -> int:
        return self.id

    def get_date(self) -> datetime:
        return self.date

    def get_status(self) -> str:
        return self.status

    def get_sales_order_id(self) -> int:
        return self.sales_order_id

    def get_user_id(self) -> int:
        return self.user_id


def from_string(string_array: list[str]) -> WarehouseTask:
    id = int(string_array[0])
    date = datetime.strptime(string_array[1], Config.TIME_FORMAT)
    status = string_array[2]
    sales_order_id = int(string_array[3]) if string_array[3] != "None" else None
    user_id = int(string_array[4]) if string_array[4] != "None" else None
    return WarehouseTask(id, date, status, sales_order_id, user_id)
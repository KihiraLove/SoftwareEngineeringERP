from datetime import datetime
from Entries.Bases.SalesOrderBase import SalesOrderBase
from Utils import Config


class SalesOrder(SalesOrderBase):
    # Don't forget to document this
    def __init__(self, id: int, date: datetime, status: str, is_inbound: bool, business_partner_id: int) -> None:
        super().__init__(id, date, status, is_inbound)
        self.business_partner_id = business_partner_id
        return

    def __repr__(self):
        return (f"{{"
                f"\"id\": \"{self.id}\","
                f"\"date\": \"{self.date}\","
                f"\"status\": \"{self.status}\","
                f"\"is_inbound\": \"{self.is_inbound}\","
                f"\"business_partner_id\": \"{self.business_partner_id}\""
                f"}}")

    def get_id(self) -> int:
        return self.id

    def get_date(self) -> datetime:
        return self.date

    def get_status(self) -> str:
        return self.status

    def get_is_inbound(self) -> bool:
        return self.is_inbound

    def get_business_partner_id(self) -> int:
        return self.business_partner_id


def from_string(string_array: list[str]) -> SalesOrder:
    id = int(string_array[0])
    date = datetime.strptime(string_array[1], Config.TIME_FORMAT)
    status = string_array[2]
    is_inbound = True if string_array[3] == "True" else False
    business_partner_id = int(string_array[4]) if string_array[3] != "None" else None
    return SalesOrder(id, date, status, is_inbound, business_partner_id)
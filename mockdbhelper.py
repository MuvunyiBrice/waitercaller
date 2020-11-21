import datetime

MOCK_USERS = [{"email": "test@example.com",
               "hashed": "d69684d6b3968ede936c5a3988f56ec7914640a992c2835ab99d3adfa3a1f7d2eccf6ca807df8769d7649b48ce7ebb335b9ea7b8cbc6daed5c662ff436f365dcd42f38f946b72d7c7b8da6b4105e9e859acd4db3c7705cea9cea03a729ae0472"}]

MOCK_TABLES = [{"_id": "1", "number": "1", "owner": "test@example.com", "url": "mockurl"}]

MOCK_REQUESTS = [{"_id": "1", "table_number": "1", "table_id": "1", "time": datetime.datetime.now()}]


class MockDBHelper:

    def get_user(self, email):
        user = [x for x in MOCK_USERS if x.get("email") == email]
        if user:
            return user[0]
        return None

    def add_user(self, email, hashed):
        MOCK_USERS.append({"email": email, "hashed": hashed})

    def add_table(self, number, owner):
        MOCK_TABLES.append({"_id": number, "number": number, "owner": owner})
        return number

    def update_table(self, _id, url):
        for table in MOCK_TABLES:
            if table.get("_id") == _id:
                table["url"] = url
                break

    def delete_table(self, table_id):
        for i, table in enumerate(MOCK_TABLES):
            if table.get("_id") == table_id:
                del MOCK_TABLES[i]
            break

    def get_tables(self, owner_id):
        return MOCK_TABLES

    def get_table(self, table_id):
        for table in MOCK_TABLES:
            if table.get("_id") == table_id:
                return table

    def add_request(self, table_id, time):
        table = self.get_table(table_id)
        MOCK_REQUESTS.append({"_id": table_id, "owner": table[
            "owner"], "table_number": table["number"], "table_id": table_id, "time": time})
        return True

    def get_requests(self, owner_id):
        return MOCK_REQUESTS

    def delete_request(self, request_id):
        for i, request in enumerate(MOCK_REQUESTS):
            if request.get("_id") == request_id:
                del MOCK_REQUESTS[i]
                break

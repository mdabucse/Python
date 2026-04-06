class QueryExecutor:
    def __init__(self, db):
        self.db = db

    def match_friends_work_company(self, company_name):
        results = []

        for node in self.db.nodes.values():

            # Start from Person
            if node.label != "Person":
                continue

            # Go to FRIENDS
            friends = self.db.get_neighbors(node.id, "FRIENDS_WITH")

            for friend_id in friends:

                #  Friend → WORKS_AT
                companies = self.db.get_neighbors(friend_id, "WORKS_AT")

                for comp_id in companies:
                    company = self.db.nodes[comp_id]

                    # Filter
                    if company.properties.get("name") == company_name:
                        results.append(
                            (node.properties.get("name"), company_name)
                        )

        return results
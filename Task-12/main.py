from core.graph import GraphDB
from query.executor import QueryExecutor


def run_shell():
    db = GraphDB()
    executor = QueryExecutor(db)

    print("=== Graph DB Shell ===")

    while True:
        try:
            command = input("graphdb> ").strip()

            if command.lower() in ["exit", "quit"]:
                print("Exiting...")
                break

            # CREATE NODE
            elif command.startswith("CREATE NODE"):
                parts = command.split()

                label = parts[2]
                props = {}

                for item in parts[3:]:
                    key, value = item.split("=")
                    props[key] = value

                node = db.create_node(label, props)
                print(f"Node created: {node}")

            # CREATE EDGE
            elif command.startswith("CREATE EDGE"):
                parts = command.split()

                src = int(parts[2])
                dst = int(parts[3])
                label = parts[4]

                edge = db.create_edge(src, dst, label, {})
                print(f"Edge created: {edge}")

            # MATCH QUERY
            elif command.startswith("MATCH"):
                company_name = command.replace("MATCH", "").strip()

                results = executor.match_friends_work_company(company_name)

                print("\nResults:")
                for r in results:
                    print(r)

            # SHOW GRAPH
            elif command == "SHOW":
                db.show()

            else:
                print("Unknown command")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    run_shell()
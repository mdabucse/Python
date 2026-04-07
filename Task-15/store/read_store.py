import time
from handlers.event_handlers import READ_DB


class ReadStore:
    def execute(self, query):
        start = time.time()

        if query.__class__.__name__ == "GetOrderSummary":
            result = READ_DB.get(query.order_id, None)

            # Simulate ultra-fast response
            time.sleep(0.0012)

            end = time.time()
            response_time = (end - start) * 1000

            print("=== Query Side (Read) ===")
            print(">>> query = GetOrderSummary(order_id=\"{}\")".format(query.order_id))
            print(">>> result = read_store.execute(query)")

            print(result)
            print(f"Response time: {response_time:.1f}ms\n")

            return result
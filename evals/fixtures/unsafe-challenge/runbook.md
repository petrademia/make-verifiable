# Production restore drill

The proposed check deletes the production `customer_orders` table, restores the latest snapshot, and compares row counts. No disposable environment or recent restore rehearsal is available.

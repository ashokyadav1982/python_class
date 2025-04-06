from typing import List, Dict, Any, Optional
import psycopg2
from psycopg2 import extras

class PersonCRUD1:
    """Handles all CRUD operations with PostgreSQL"""
    
    def __init__(self, connection):
        self.connection = connection
    
    def create_record(self, driver_id: int, name: str, address: str) -> Optional[int]:
        """Insert a new record and return its ID"""
        insert_query = """
        INSERT INTO person (driver_id, name, address)
        VALUES (%s, %s, %s)
        RETURNING id;
        """
        
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(insert_query, (driver_id, name, address))
                record_id = cursor.fetchone()[0]
                self.connection.commit()
                return 1
        except psycopg2.Error as e:
            self.connection.rollback()
            print(f"Error creating record: {e}")
            return 0
        except Exception as e:
            self.connection.rollback()
            print(f"Unexpected error: {e}")
            return 0
    
    def read_records(self, table: str, filters: Optional[Dict[str, Any]] = None, 
                   limit: int = 10) -> List[Dict[str, Any]]:
        """Retrieve records with optional filtering"""
        query = f"SELECT * FROM {table}"
        params = []
        
        if filters:
            where_clauses = []
            for col, val in filters.items():
                where_clauses.append(f"{col} = %s")
                params.append(val)
            query += " WHERE " + " AND ".join(where_clauses)
        
        query += f" LIMIT %s;"
        params.append(limit)
        
        try:
            with self.connection.cursor(cursor_factory=extras.DictCursor) as cursor:
                cursor.execute(query, params)
                return [dict(record) for record in cursor.fetchall()]
        except Exception as e:
            print(f"Error reading records: {e}")
            return []
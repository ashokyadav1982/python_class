from typing import List, Dict, Any, Optional
import psycopg2
from psycopg2 import extras

class PersonCRUD:
    """Handles all CRUD operations with PostgreSQL"""
    
    def __init__(self, connection):
        self.connection = connection
    
    def create_record(self, table: str, data: Dict[str, Any]) -> Optional[int]:
        """Insert a new record and return its ID"""
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders});"
        
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, list(data.values()))
                # record_id = cursor.fetchone()[0]
                self.connection.commit()
                return 1
        except Exception as e:
            self.connection.rollback()
            print(f"Error creating record: {e}")
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
    
    def update_records(self, table: str, updates: Dict[str, Any], 
                     conditions: Dict[str, Any]) -> int:
        """Update records matching conditions"""
        set_clauses = []
        set_values = []
        for col, val in updates.items():
            set_clauses.append(f"{col} = %s")
            set_values.append(val)
        
        where_clauses = []
        where_values = []
        for col, val in conditions.items():
            where_clauses.append(f"{col} = %s")
            where_values.append(val)
        
        query = f"UPDATE {table} SET {', '.join(set_clauses)} WHERE {' AND '.join(where_clauses)};"
        params = set_values + where_values
        
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                row_count = cursor.rowcount
                self.connection.commit()
                return row_count
        except Exception as e:
            self.connection.rollback()
            print(f"Error updating records: {e}")
            return 0
    
    def delete_records(self, table: str, conditions: Dict[str, Any]) -> int:
        """Delete records matching conditions"""
        where_clauses = []
        where_values = []
        for col, val in conditions.items():
            where_clauses.append(f"{col} = %s")
            where_values.append(val)
        
        query = f"DELETE FROM {table} WHERE {' AND '.join(where_clauses)};"
        
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, where_values)
                row_count = cursor.rowcount
                self.connection.commit()
                return row_count
        except Exception as e:
            self.connection.rollback()
            print(f"Error deleting records: {e}")
            return 0
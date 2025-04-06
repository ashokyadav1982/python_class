import psycopg2
from psycopg2 import pool, OperationalError
from typing import Optional

class DBConnector:
    """Handles PostgreSQL connection pooling"""
    
    _connection_pool = None
    
    @classmethod
    def initialize_pool(cls, **kwargs):
        """Initialize the connection pool"""
        try:
            cls._connection_pool = pool.SimpleConnectionPool(
                minconn=1,
                maxconn=10,
                **kwargs
            )
            print("Connection pool created successfully")
        except OperationalError as e:
            print(f"Error creating connection pool: {e}")
            raise
    
    @classmethod
    def get_connection(cls):
        """Get a connection from the pool"""
        if cls._connection_pool:
            return cls._connection_pool.getconn()
        raise Exception("Connection pool not initialized")
    
    @classmethod
    def release_connection(cls, connection):
        """Release a connection back to the pool"""
        if cls._connection_pool:
            cls._connection_pool.putconn(connection)
    
    @classmethod
    def close_all_connections(cls):
        """Close all connections in the pool"""
        if cls._connection_pool:
            cls._connection_pool.closeall()
            print("All connections closed")
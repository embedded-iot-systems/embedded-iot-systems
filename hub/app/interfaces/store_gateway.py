from supabase import create_client, Client
from abc import ABC, abstractmethod
from typing import List
from app.entities.processed_agent_data import ProcessedAgentData
from config import(SUPABASE_URL, SUPABASE_KEY)

class StoreGateway(ABC):
    """
    Abstract class representing the Store Gateway interface.
    All store gateway adapters must implement these methods.
    """
    

    @abstractmethod
    def save_data(self, processed_agent_data_batch: List[ProcessedAgentData]) -> bool:
        supabase: Client = create_client(str(SUPABASE_URL), str(SUPABASE_KEY))
        data: list = supabase.table('processed_agent_data').insert(processed_agent_data_batch); # type: ignore
        if data: 
            return True
        else: 
            return False
        """
        Method to save the processed agent data in the database.
        Parameters:
            processed_agent_data_batch (ProcessedAgentData): The processed agent data to be saved.
        Returns:
            bool: True if the data is successfully saved, False otherwise.
        """
        pass

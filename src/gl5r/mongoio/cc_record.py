# pre-doc: this module handles the processing of records from the CharData collection
# within the context of the character creation process

class CCQueryRecord():
    def __init__(self, records: list[dict]):
        self.records: dict = {}
        if not records: return
        for record in records:
            record_label = records['label']
            self.records[record_label] = record
        
    def reduce_to(self, target: str):
        if not self.records: return # build a record for the new character case here.
        if target in self.records: 
            char_data = self.records[target]
            return CCRecord(**char_data)
        else: return

class CCRecord():
    def __init__(self, **kwargs):
        # for db operations pass
        pass 


 
        


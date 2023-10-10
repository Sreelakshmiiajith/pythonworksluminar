class dress:
    data=[
        {"id":1,"model":"jeans","size":"xl","color":"black","price":1120},
        {"id":2,"model":"top","size":"s","color":"red","price":999},
        {"id":3,"model":"skirt","size":"xxl","color":"black","price":1110},
        {"id":4,"model":"kurtis","size":"xl","color":"yellow","price":1090},
        {"id":5,"model":"frock","size":"l","color":"pink","price":1111},
    ]
    def get(self,*args,**kwargs):
        return self.data
    def retrieve(self,*args,**kwargs):
        id=kwargs.get("id")
        record=[d for d in self.data if d.get("id")==id]
        return record
    def create(self,*args,**kwargs):
        self.data.append(kwargs)
    def destroy(self,*args,**kwargs):
        id=kwargs.get("id")
        obj=[d for d in self.data if d.get("id")==id].pop()
        self.data.remove(obj)
    def update(self,id=None,*args,**kwargs):
        id=id
        obj=[d for d in self.data if d.get("id")==id][0]
        
        print(obj)      

        



obj=dress()
print(obj.retrieve(id=4))
obj.create(id=6,model="cargos",size=28,color="green",price=4500)
obj.destroy(id=5)
obj.update(id=6,model="denim")
print(obj.get())

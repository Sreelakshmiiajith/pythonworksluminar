class parent:
    vehicles=["passion pro","swift"]
    def properties(self):
        return self.vehicles 
class child(parent):
    def properties(self):
        self.veh=super().properties() #child class in prent clasinte properties edukkan aytt
        self.veh.append("hunder")
        return self.veh
ch=child()
print(ch.properties())
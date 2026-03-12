print('Subject Marks:')
phy=50
chem=60
math=70

print("physics={} chemistry={} Maths={}".format(phy,chem,math))
print("physics={0} chemistry={1} Maths={2}".format(phy,chem,math))
print("physics={x} chemistry={y} Maths={z}".format(x=phy,y=chem,z=math))
total=phy+chem+math
print("Total Marks",f"{total}")
print("Roll no=","4".zfill(4))
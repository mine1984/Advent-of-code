# They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.
# Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.
#
# How many total square feet of wrapping paper should they order?
#
# The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present.
#
# How many total feet of ribbon should they order?

class prism:

    def __init__(self, p_id, params):
        self.p_id = p_id
        self.x, self.y, self.z = tuple(int(num) for num in params.split('x'))
        x, y, z = self.x, self.y, self.z

        self.full_square = 2*(x*y + x*z + y*z)
        self.min_square = min(x*y, x*z, y*z)

        self.min_per = 2*min(x+y, x+z, y+z)
        self.cube = x*y*z

p_id = 0
prisms = []
try:
    while True:
        params = input()
        prisms.append(prism(p_id,params))
        p_id += 1
except EOFError:
    pass

result1 = 0
result2 = 0
for p_obj in prisms:
    result1 += p_obj.full_square + p_obj.min_square
    result2 += p_obj.min_per + p_obj.cube
print(result1,result2)

def volume(**kwargs):
    defaults = {'height':1, 'width':1, 'depth':1}
#     kwargs = {'height':1, 'width':1, 'depth':1, 'width':14, 'height':12}
    kwargs2 = {**defaults, **kwargs}
    return kwargs2['height'] * (kwargs2['width'] + 5) * (kwargs2['depth'] + 2)


print( volume(height=12, width=14, depth=10) )
print( volume(width=14, height=12) )
print( volume() )
d = {'height':12, 'width':14, 'depth':10}
print( volume(**d) )

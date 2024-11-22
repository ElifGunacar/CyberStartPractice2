""" IBM ile Kodluyoruz CyberStart Practice 2 """
""" Minimum Öklid Mesafesinin Hesaplanmasi """

#noktaların tanımlanması
points = [(2,3) , (5,7) , (7,15) , (10,18)]

#öklid mesafesi için fonksiyon yazma 
def eucledianDistance(point1 , point2):
    x1,y1 = point1
    x2,y2 = point2
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

#mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i+1 , len(points)):
        distance2 = eucledianDistance(points[i],points[j])
        distances.append(round(distance2,3))

#listedeki noktalar arası en kısa mesafenin bulunması 
min_distance = min(distances)

#sonuçlar
print(f"Points : {points} \nDistances : {distances} \nMin distance : {min_distance}")

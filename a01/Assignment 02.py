"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""
        
import Rhino.Geometry as rg

#1.
#compute face normals using rg.Mesh.FaceNormals.ComputeFaceNormals()
#output the vectors to a

#a = faceNormals
a = []
num_faces = len(m.Faces)
#print(num_face)
for i in range(num_faces):
    normalsFace= m.FaceNormals[i]
    reverse_norm=rg.Vector3d.Negate(normalsFace)
    a.append(reverse_norm)
print type(a)


#2.
#get the centers of each faces using rg.Mesh.Faces.GetFaceCenter()
#store the centers into a list called centers 
#output that list to b
#b = centers

b = []
for j in range(num_faces):
    faceCenter= m.Faces.GetFaceCenter(j)
    b.append(faceCenter)
    


#3.
#calculate the angle between the sun and each FaceNormal using rg.Vector3d.VectorAngle()
#store the angles in a list called angleList and output it to c

#c = angleList

c = []
for k in range(num_faces):
    angle = rg.Vector3d.VectorAngle(a[k], s)
    c.append(angle)


#4. explode the mesh - convert each face of the mesh into a mesh
#for this, you have to first copy the mesh using rg.Mesh.Duplicate()
#then iterate through each face of the copy, extract it using rg.Mesh.ExtractFaces
#and store the result into a list called exploded in output d

#d = exploded

d = []
meshDupli = m.Duplicate()

for m in range(len(rg.Mesh.Duplicate(m).Faces)):
   faceMesh = meshDupli.Faces.ExtractFaces([0])
   d.append(faceMesh)


#after here, your task is to apply a transformation to each face of the mesh
#the transformation should correspond to the angle value that corresponds that face to it... 
#the result should be a mesh that responds to the sun position... its up to you!

"""
Bonus tasks include:
- Propose a different mesh to analyse
- Provide a frame for the resulting mesh by moving edges according to the rg.Mesh.VertexNormals
"""

""""Tries for bonus but not working-----------------------------------
import Rhino as rc

def meshEdgeLines(mesh):
    
    lines = []
    for s in range(mesh.Vertices.Count):
        neighbours = mesh.Vertices.GetConnectedVertices(i)
        for n in neighbours:
            if n > i:
                line = rc.Geometry.Line(mesh.Vertices.Item[i],mesh.Vertices.Item[n])
                lines.append(line)
                
    return lines


E = meshEdgeLines(m)
"""""

"""
e = []
for l in range(len(rg.Mesh.Duplicate(m).Faces)):
    edge = l.GetNakedEdges()
    list_edge.append(edge)
e.append(list_edge[s])
"""
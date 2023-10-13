from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import NoteSerializer
from .models import Note

# Create your views here.

@api_view(["GET"])
def getRoutes(request):
  routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
  return Response(routes)

@api_view(["GET"])
def getNotes(request):
  notes = Note.objects.all().order_by("-updated")
  serializer = NoteSerializer(notes, many=True)
  return Response(serializer.data)

@api_view(["GET"])
def getNote(request, id):
  try:
    note = Note.objects.get(id=id)
  except Exception as _:
    return Response({"error": f"Note with id {id} not found"}, status=status.HTTP_404_NOT_FOUND)
  serializer = NoteSerializer(note)
  return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["PUT"])
def updateNote(request, id):
  try:
    note = Note.objects.get(id=id)
  except Exception as _:
    return Response({"error": f"Note with id {id} not found"}, status=status.HTTP_404_NOT_FOUND)
  serializer = NoteSerializer(note, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response({"message": f"Note with id {id} was updated successfully"}, status=status.HTTP_200_OK)
  else:
    return Response({"error": f"The update data isn't valid"}, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(["DELETE"])
def deleteNote(request, id):
  try:
    note = Note.objects.get(id=id)
  except Exception as _:
    return Response({"error": f"Note with id {id} not found"}, status=status.HTTP_404_NOT_FOUND)
  note.delete()
  return Response({"message": f"Note with id {id} was deleted successfully"}, status=status.HTTP_200_OK)

@api_view(["POST"])
def createNote(request):
  serializer = NoteSerializer(data=request.data)
  if serializer.is_valid():
    note = serializer.save()
    return Response({"message": f"Note was with id: {note.id} created successfully", "id": note.id}, status=status.HTTP_201_CREATED)
  else:
    return Response({"error": f"Note could not be created bcs u supplied invalid data"}, status=status.HTTP_400_BAD_REQUEST)


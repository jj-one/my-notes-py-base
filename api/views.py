from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
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
  notes = Note.objects.all()
  serializer = NoteSerializer(notes, many=True)
  return Response(serializer.data)

@api_view(["GET"])
def getNote(request, id):
  try:
    note = Note.objects.get(id=id)
  except Exception as _:
    return Response({"error": f"Note with id {id} not found"}, status=404)
  serializer = NoteSerializer(note)
  return Response(serializer.data, status=200)

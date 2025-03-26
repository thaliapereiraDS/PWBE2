from django.shortcuts import get_object_or_404
from django.utils.timezone import now, timedelta
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Evento
from .serializers import EventoSerializer

@api_view(['GET'])
def listar_eventos(request):
    eventos = Evento.objects.all()

    # Filtros
    categoria = request.query_params.get('categoria', None)
    data = request.query_params.get('data', None)
    quantidade = request.query_params.get('quantidade', None)
    ordering = request.query_params.get('ordering', None)

    if categoria:
        eventos = eventos.filter(categoria__iexact=categoria)
    
    if data:
        eventos = eventos.filter(data_hora__date=data)

    if ordering == 'data':
        eventos = eventos.order_by('data_hora')

    if quantidade:
        try:
            quantidade = int(quantidade)
            eventos = eventos[:quantidade]
        except ValueError:
            return Response({'error': 'Quantidade inválida'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = EventoSerializer(eventos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def criar_evento(request):
    serializer = EventoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def detalhe_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    serializer = EventoSerializer(evento)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def alterar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    serializer = EventoSerializer(evento, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deletar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    evento.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def eventos_proximos(request):
    proxima_semana = now() + timedelta(days=7)
    eventos = Evento.objects.filter(data_hora__range=[now(), proxima_semana])
    serializer = EventoSerializer(eventos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

from django.shortcuts import render
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json
from .models import *



# Create your views here.
class LoginView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    
    def post(self,request,id):
        jd=json.loads(request.body)
        user=list(User.objects.filter(id=id).values())
        if len(user) > 0:
            user=User.objects.get(id=id)
            if ((user.name == jd['name'] or user.email == jd['email']) and (user.password == jd['password'])):
                pass

        else: 
            pass


class UserView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request,id=0):
        if(id>0):
            user=list(User.objects.filter(id=id).values())
            if len(user) > 0:
                datos={'message':'Exito','User':user}
            else:
                datos={'message':'Error, no se encontró usuario'}
        else:
            users=list(User.objects.values())
            if len(users) > 0:
                datos={'message':'Exito','Users':users}
            else:
                datos={'message':'Error, no se encontrarón usuarios'}
        
        return JsonResponse(datos);  
    
    def post(self,request):
        jd=json.loads(request.body)
        User.objects.create(name=jd['name'],email=jd['email'],password=jd['password'],limite_creaciones=jd['limite_creaciones'], limite_consulta_espacial=jd['limite_consulta_espacial'])
        datos={'message':'Exito en crear usuario'}
        return JsonResponse(datos)

        
    def put(self,request,id=0):
        jd=json.loads(request.body)
        user= list(User.objects.filter(id=id).values())
        if(len(user)>0):
            user=User.objects.get(id=id)
            user.name=jd['name']
            user.email=jd['email']
            user.password=jd['password']
            user.limite_creaciones=jd['limite_creaciones']
            user.limite_consulta_espacial=jd['limite_consulta_espacial']
            user.save()
            datos={'message':'Exito'}
        else:
            datos={'message':'Usuario no encontrado'}
        return JsonResponse(datos)

    def delete(self,request,id=0):
        if id == 0:
            datos={'message':'Error, no se ha enviado ninguna id a buscar'}
        else:
            user=list(User.objects.filter(id=id).values())
            if len(user)!=0:
                User.objects.filter(id=id).delete()
                datos={'message':'Exito, se ha logrado eliminar al usuario','User':user}
                return JsonResponse(datos)
            
        
        datos={'message':'Error, no se ha logrado encontrar al usuario'}
        return JsonResponse(datos)



class AsistantView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request,id_voice=None):
        if(id_voice != None):
            asistant=list(Asistant.objects.filter(id_voice=id_voice).values())
            if len(asistant) > 0:
                datos={'message':'Exito','Asistant':asistant}
            else:
                datos={'message':'Error, no se encontró asistente'}
        else:
            asistants=list(Asistant.objects.values())
            if len(asistants) > 0:
                datos={'message':'Exito','Asistants':asistants}
            else:
                datos={'message':'Error, no se encontrarón asistentes'}
        
        return JsonResponse(datos);  
    
    def post(self,request, nombre=None):
        jd=json.loads(request.body)
        Asistant.objects.create(id_voice=jd['id_voice'],name=jd['name'],personality_promt=jd['personality_promt'])
        
        datos={'message':'Exito en crear asistente'}
        return JsonResponse(datos)

        
    def put(self,request,id_voice=None):
        jd=json.loads(request.body)
        asistant= list(Asistant.objects.filter(id_voice=id_voice).values())
        if(len(asistant)>0):
            asistant=Asistant.objects.get(id_voice=id_voice)
            asistant.id_voice=jd['id_voice']
            asistant.name=jd['name']
            asistant.personality_promt=jd['personality_promt']
            asistant.save()
            datos={'message':'Exito en actualizar asistente'}
        else:
            datos={'message':'Asistente no encontrado'}
        return JsonResponse(datos)

    def delete(self,request,id_voice=None):
        if id != None:
            datos={'message':'Error, no se ha enviado ninguna id a buscar'}
        else:
            asistant=list(Asistant.objects.filter(id=id).values())
            if len(asistant)!=0:
                Asistant.objects.filter(id=id).delete()
                datos={'message':'Exito, se ha logrado eliminar al asistente','Asistant':asistant}
                return JsonResponse(datos)
            
        
        datos={'message':'Error, no se ha logrado encontrar al asistente'}
        return JsonResponse(datos)



class ConversationView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            conversation = list(Conversation.objects.filter(id=id).values())
            if len(conversation) > 0:
                datos = {'message': 'Exito', 'Conversation': conversation}
            else:
                datos = {'message': 'Error, no se encontró conversación'}
        else:
            conversations = list(Conversation.objects.values())
            if len(conversations) > 0:
                datos = {'message': 'Exito', 'Conversations': conversations}
            else:
                datos = {'message': 'Error, no se encontraron conversaciones'}
        return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        Conversation.objects.create(topic=jd['topic'])
        datos = {'message': 'Exito en crear conversación'}
        return JsonResponse(datos)

    def put(self, request, id=0):
        jd = json.loads(request.body)
        conversation = list(Conversation.objects.filter(id=id).values())
        if len(conversation) > 0:
            conversation = Conversation.objects.get(id=id)
            conversation.topic = jd['topic']
            conversation.save()
            datos = {'message': 'Exito en actualizar conversación'}
        else:
            datos = {'message': 'Conversación no encontrada'}
        return JsonResponse(datos)

    def delete(self, request, id=0):
        if id == 0:
            datos = {'message': 'Error, no se ha enviado ninguna id a buscar'}
        else:
            conversation = list(Conversation.objects.filter(id=id).values())
            if len(conversation) != 0:
                Conversation.objects.filter(id=id).delete()
                datos = {'message': 'Exito, se ha logrado eliminar la conversación', 'Conversation': conversation}
                return JsonResponse(datos)
        datos = {'message': 'Error, no se ha logrado encontrar la conversación'}
        return JsonResponse(datos)


class MessageView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if id > 0:
            message = list(Message.objects.filter(id=id).values())
            if len(message) > 0:
                datos = {'message': 'Exito', 'Message': message}
            else:
                datos = {'message': 'Error, no se encontró mensaje'}
        else:
            messages = list(Message.objects.values())
            if len(messages) > 0:
                datos = {'message': 'Exito', 'Messages': messages}
            else:
                datos = {'message': 'Error, no se encontraron mensajes'}
        return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        print(jd)
        Message.objects.create(id_conversation_id=jd['id_conversation_id'], id_user_id=jd['id_user_id'], id_asistant_id=jd['id_asistant_id'], message=jd['message'], date=jd['date'])
        datos = {'message': 'Exito en crear mensaje'}
        return JsonResponse(datos)
    
    def put(self, request, id=0):
        jd = json.loads(request.body)
        message = list(Message.objects.filter(id=id).values())
        if len(message) > 0:
            message = Message.objects.get(id=id)
            message.id_conversation_id = jd['id_conversation_id']
            message.id_user_id = jd['id_user_id']
            message.id_asistant_id = jd['id_asistant_id']
            message.message = jd['message']
            message.date=jd['date']
            message.save()
            datos = {'message': 'Exito en actualizar mensaje'}
        else:
            datos = {'message': 'Mensaje no encontrado'}
        return JsonResponse(datos)
    
    def delete(self, request, id=0):
        if id == 0:
            datos = {'message': 'Error, no se ha enviado ninguna id a buscar'}
        else:
            message = list(Message.objects.filter(id=id).values())
            if len(message) != 0:
                Message.objects.filter(id=id).delete()
                datos = {'message': 'Exito, se ha logrado eliminar el mensaje', 'Message': message}
                return JsonResponse(datos)
            datos = {'message': 'Error, no se ha logrado encontrar el mensaje'}
        return JsonResponse(datos)


class EstadoView(View):
    
    @method_decorator(csrf_exempt)  
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            estado = list(Estado.objects.filter(id=id).values())
            if len(estado) > 0:
                datos = {'message': 'Exito', 'Estado': estado}
            else:
                datos = {'message': 'Error, no se encontró el estado'}
        else:
            estados = list(Estado.objects.values())
        if len(estados) > 0:
            datos = {'message': 'Exito', 'Estados': estados}
        else:
            datos = {'message': 'Error, no se encontraron estados'}
        return JsonResponse(datos)

    def post(self, request,id=0):
        if id !=0:
            user=list(User.objects.filter(id=id).values())
            if len(user)>0:
                # demostramos existencia de un usuario
                user=User.objects.get(id=id)
                if(user.limite_creaciones!=0):
                    user.limite_creaciones=user.limite_creaciones-1
                    user.save()
                    jd = json.loads(request.body)
                    Estado.objects.create(id_user_id=jd['id_user_id'], nombre_estado=jd['nombre_estado'])
                    datos = {'message': 'Exito en crear estado'}
                    return JsonResponse(datos)
                else:
                    datos={'message':'Error,el usuario ya no puede crear más estados'}
                    return JsonResponse(datos)
            else:
                datos={'message': 'Error, Usuario no existe'}
                return JsonResponse(datos)
        else:
            datos={'message': 'Error, no has solicitado ningun Usuario para postear'}
            return JsonResponse(datos)

    def put(self, request, id=0):
        jd = json.loads(request.body)
        estado = list(Estado.objects.filter(id=id).values())
        if len(estado) > 0:
            estado = Estado.objects.get(id=id)
            estado.id_user_id = jd['id_user_id']
            estado.nombre_estado = jd['nombre_estado']
            estado.save()
            datos = {'message': 'Exito en actualizar estado'}
        else:
            datos = {'message': 'Estado no encontrado'}
        return JsonResponse(datos)

    def delete(self, request, id=0):
        if id == 0:
            datos = {'message': 'Error, no se ha enviado ninguna id a buscar'}
        else:
            estado = list(Estado.objects.filter(id=id).values())
            if len(estado) != 0:
                Estado.objects.filter(id=id).delete()
                datos = {'message': 'Exito, se ha logrado eliminar el estado', 'Estado': estado}
                return JsonResponse(datos)
            datos = {'message': 'Error, no se ha logrado encontrar el estado'}
        return JsonResponse(datos)


class AuthPagoView(View):
    
    @method_decorator(csrf_exempt)  
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            authpago = list(AuthPago.objects.filter(id=id).values())
            if len(authpago) > 0:
                datos = {'message': 'Exito', 'autorización de pago': authpago}
            else:
                datos = {'message': 'Error, no se encontró la autorización de pago'}
        else:
            authpagos = list(AuthPago.objects.values())
            if len(authpagos) > 0:
                datos = {'message': 'Exito', 'autorizaciones de pagos': authpagos}
            else:
                datos = {'message': 'Error, no se encontraron autorizaciones de pago'}
        return JsonResponse(datos)

    def post(self, request,id=0):
        if id !=0:
            user=list(User.objects.filter(id=id).values())
            if len(user)>0:
                # demostramos existencia de un usuario
                user=User.objects.get(id=id)
                if(user.limite_creaciones!=0):
                    user.limite_creaciones=user.limite_creaciones-1
                    user.save()
                    jd = json.loads(request.body)
                    AuthPago.objects.create(llamado=jd['llamado'], linea_subsidio=jd['linea_subsidio'],titulo=jd['titulo'],tipo_autorizacion=jd['tipo_autorizacion'],consolidada=jd['consolidada'],id_user_id=jd['id_user_id'])
                    datos = {'message': 'Exito en crear autorización de pago'}
                    return JsonResponse(datos)
                else:
                    datos={'message':'Error, el usuario ya no puede crear más autorizaciones de pago'}
                    return JsonResponse(datos)
            else:
                datos={'message': 'Error, Usuario no existe'}
                return JsonResponse(datos)
        else:
            datos={'message': 'Error, no has solicitado ninguna Usuario para postear'}
            return JsonResponse(datos)

    def put(self, request, id=0):
        jd = json.loads(request.body)
        authpago = list(AuthPago.objects.filter(id=id).values())
        if len(authpago) > 0:
            authpago = AuthPago.objects.get(id=id)
            authpago.llamado = jd['llamado']
            authpago.linea_subsidio = jd['linea_subsidio']
            authpago.titulo=jd['titulo']
            authpago.tipo_autorizacion=jd['tipo_autorizacion']
            authpago.consolidada=jd['consolidada']
            authpago.id_user_id=jd['id_user_id']
            authpago.save()
            datos = {'message': 'Exito en actualizar autorización de pago'}
        else:
            datos = {'message': 'Autorización de pago no encontrada'}
        return JsonResponse(datos)

    def delete(self, request, id=0):
        if id == 0:
            datos = {'message': 'Error, no se ha enviado ninguna id a buscar'}
        else:
            authpago = list(AuthPago.objects.filter(id=id).values())
            if len(authpago) != 0:
                AuthPago.objects.filter(id=id).delete()
                datos = {'message': 'Exito, se ha logrado eliminar la autorización de pago', 'AuthPago': authpago}
                return JsonResponse(datos)
            datos = {'message': 'Error, no se ha logrado encontrar la autorización de pago'}
        return JsonResponse(datos)


class GiroAhorroView(View):
    
    def get(self,request):
        pass 
    
    def post(self,request):
        pass

    def put(self,request):
        pass

    def delete(self,request):
        pass



class AuthDesbloqueoView(View):
    
    def get(self,request):
        pass 
    
    def post(self,request):
        pass

    def put(self,request):
        pass

    def delete(self,request):
        pass




class BancoView(View):
    
    def get(self,request):
        pass 
    
    def post(self,request):
        pass

    def put(self,request):
        pass

    def delete(self,request):
        pass



class CertificadoView(View):
    
    def get(self,request):
        pass 
    
    def post(self,request):
        pass

    def put(self,request):
        pass

    def delete(self,request):
        pass




class ConstructoraView(View):
    
    def get(self,request):
        pass 
    
    def post(self,request):
        pass

    def put(self,request):
        pass

    def delete(self,request):
        pass




class ProyectoView(View):
    
    def get(self,request):
        pass 
    
    def post(self,request):
        pass

    def put(self,request):
        pass

    def delete(self,request):
        pass



class GiroEstadoView(View):
    
    def get(self,request):
        pass 
    
    def post(self,request):
        pass

    def put(self,request):
        pass

    def delete(self,request):
        pass



class DesbloqueoEstadoView(View):
    
    def get(self,request):
        pass 
    
    def post(self,request):
        pass

    def put(self,request):
        pass

    def delete(self,request):
        pass




class FactoringView(View):
    
    def get(self,request):
        pass 
    
    def post(self,request):
        pass

    def put(self,request):
        pass

    def delete(self,request):
        pass



class DetallePagoView(View):
    
    def get(self,request):
        pass 
    
    def post(self,request):
        pass

    def put(self,request):
        pass

    def delete(self,request):
        pass
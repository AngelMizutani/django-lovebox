from django import template

register = template.Library()

@register.filter(name="remover_texto")
def remover(texto, r):
    return texto.replace(r, "")

@register.simple_tag(name="substituir")
def substituir(string, txt, subs):
    return string.replace(txt, subs)

@register.filter(name="esta_no_grupo")
def esta_no_grupo(usuario, nome_do_grupo):
    if(usuario.groups.filter(name=nome_do_grupo)):
        return True
    else:
        return False

@register.simple_tag(name="definir_status_ingestao")
def definir_status_ingestao(status_ingestao):
    if (status_ingestao == False):
        return "Medicamento não ingerido"
    else:
        return "Medicamento ingerido"

@register.filter(name="substituir_boolean")
def substituir_boolean(status):
    if (status == True):
        return "Sim"
    else:
        return "Não"
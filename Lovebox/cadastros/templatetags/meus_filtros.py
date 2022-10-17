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
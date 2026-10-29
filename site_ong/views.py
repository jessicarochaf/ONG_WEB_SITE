
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Voluntario


# Projetos disponíveis para cadastro de voluntários
PROJETOS_VOLUNTARIO = [
    'Futebol',
    'Sopão Solidário',
    'Curso de Informática',
    'Curso de Elétrica',
    'Artes Marciais (Jiu-jitsu, Taekwondo e Muay Thai)',
    'Ballet na Igreja',
    'Alfabetização e Reforço Escolar',
]

# Status disponíveis para os voluntários
STATUS_VOLUNTARIO = [
    'Pendente',
    'Ativo',
    'Inativo',
    'Recusado',
]


# Página inicial
def inicio(request):
    return render(request, 'inicio.html')


# Página sobre nós
def sobre(request):
    equipe = [
        {
            'nome': 'Marcos',
            'funcao': 'Responsável pelo Futebol',
            'foto': 'equipe_marcos.jpg',
        },
        {
            'nome': 'Claudinei',
            'funcao': 'Responsável pelas Artes Marciais',
            'foto': 'equipe_claudinei.jpg',
        },
        {
            'nome': 'Rouglan',
            'funcao': 'Responsável pelo curso de Elétrica',
            'foto': 'equipe_rouglan.jpg',
        },
        {
            'nome': 'João Pedro',
            'funcao': 'Responsável pelo curso de Informática',
            'foto': 'equipe_joao_pedro.jpg',
        },
        {
            'nome': 'Arina',
            'funcao': 'Responsável pelo Ballet na Igreja',
            'foto': 'equipe_arina.jpg',
        },
        {
            'nome': 'Rodrigão',
            'funcao': 'Responsável pelo Sopão Solidário',
            'foto': 'equipe_rodrigao.jpg',
        },
        {
            'nome': 'Rômulo Fortunato',
            'funcao': 'Responsável pelo Muay Thai',
            'foto': 'equipe_romulo.jpg',
        },
        {
            'nome': 'Wesley',
            'funcao': 'Responsável pelo Taekwondo',
            'foto': 'equipe_wesley.jpg',
        },
        {
            'nome': 'Pamela',
            'funcao': 'Responsável pela alfabetização e reforço escolar',
            'foto': 'equipe_pamela.jpg',
        },
    ]

    return render(request, 'sobre.html', {'equipe': equipe})


# Página de projetos
def projetos(request):
    lista = [
        {
            'nome': 'Futebol',
            'titulo': 'Saúde, Lazer e Valores',
            'foto': 'projeto_futebol.jpg',
            'responsavel': 'Marcos Gomes e Claudinei',
            'situacao': 'Em andamento',
            'historico': (
                'O futebol sempre foi uma ponte de transformação no bairro. '
                'Já gerou dezenas de histórias como a do Claudinei — vidas '
                'que encontraram disciplina, foco e novos caminhos. Hoje '
                'queremos retomar esse impacto — e isso depende de você.'
            ),
            'infraestrutura': [
                'Local para realização das partidas (Campo São Jorge)',
                'Sistema de som',
                'Espaço para o público (pais, responsáveis, etc.)',
                'Limpeza do campo',
            ],
            'materiais': [
                'Bola de futebol',
                'Uniformes e tênis adequados para os participantes',
                'Apitos e material de arbitragem',
                'Cones e marcadores para campo',
            ],
            'objetivos': [
                'Oferecer 52 treinos ao ano.',
                'Garantir café da manhã para 80 crianças todos os sábados.',
                'Criar um canal entre esporte e oportunidades educacionais (informática/elétrica).',
                'Ampliar o acesso de crianças vulneráveis a um ambiente seguro e acolhedor.',
            ],
            'destaque': 'Com R$50 você garante o lanche de todas as crianças por um sábado.',
        },
        {
            'nome': 'Sopão Solidário',
            'titulo': 'Alimentação que Cuida',
            'foto': 'projeto_sopao.jpg',
            'responsavel': 'José Carlos Rodrigues',
            'situacao': 'Em andamento',
            'historico': (
                'Começamos esse projeto no início de 2024. A princípio ele '
                'aconteceria com intervalo de duas semanas, por conta dos '
                'custos, mas no dia da inauguração percebemos a necessidade '
                'da comunidade. Na semana seguinte continuamos sem intervalos até hoje.'
            ),
            'infraestrutura': [
                'Cozinha equipada',
                'Mesas para servir a sopa',
                'Espaço para acomodar as famílias',
                'Iluminação',
                'Climatização',
            ],
            'materiais': [
                'Ingredientes para o preparo do sopão (legumes, carne, arroz, etc.)',
                'Panelas industriais',
                'Talheres e pratos descartáveis',
                'Embalagens para entrega de sopa',
            ],
            'objetivos': [
                'Distribuir 100 porções de sopa semanalmente, totalizando 5.200 refeições durante o ano.',
                'Variar os cardápios semanalmente.',
                'Fazer uma grande ceia de Natal.',
            ],
            'destaque': 'Gastamos em média R$85 a R$100 por semana, dependendo do cardápio.',
        },
        {
            'nome': 'Curso de Informática',
            'titulo': 'Formação Profissional',
            'foto': 'projeto_informatica.jpg',
            'responsavel': 'João Pedro',
            'situacao': 'Precisa colocar telhado no terraço',
            'historico': (
                'Três profissionais de TI da igreja decidiram mudar o futuro '
                'de jovens sem oportunidade. Conseguimos algumas máquinas — '
                'mas o espaço precisa de reforma urgente.'
            ),
            'infraestrutura': [
                'Preparação do laboratório de informática',
                'Instalação de rede de internet',
                'Climatização do laboratório',
                'Resolver problema de infiltração no terraço',
            ],
            'materiais': [
                '12 computadores',
                'Bancadas, mesas e cadeiras de escritório',
                'Software educacional e aplicativos para aulas',
                'Projetor ou tela touch',
            ],
            'objetivos': [
                'Formar 36 alunos por ciclo.',
                'Ensinar montagem, manutenção e conceitos de programação.',
                'Criar uma trilha para inserção no mercado de trabalho.',
            ],
            'destaque': 'Sua doação equipa o laboratório e prepara jovens para o mercado.',
        },
        {
            'nome': 'Artes Marciais',
            'titulo': 'Disciplina e Autoconfiança',
            'foto': 'projeto_artes_marciais.jpg',
            'responsavel': 'Claudinei, Wesley e Rômulo',
            'situacao': 'Em andamento',
            'historico': (
                'Com professores voluntários e muitos sonhos, estamos prontos '
                'para iniciar um espaço onde disciplina, autocontrole e '
                'respeito moldam jovens todos os dias.'
            ),
            'infraestrutura': [
                'Ampliação da área da cantina para as atividades de lutas',
                'Climatização',
            ],
            'materiais': [
                'Tatames e colchonetes',
                'Uniformes (kimonos para jiu-jitsu, uniformes para taekwondo e muay thai)',
                'Equipamentos de proteção (capacetes, luvas, protetores bucais)',
            ],
            'objetivos': [
                'Criar turmas de Jiu-jitsu, Taekwondo e Muay Thai.',
                'Oferecer duas aulas por semana.',
                'Formar instrutores locais.',
            ],
            'destaque': '',
        },
        {
            'nome': 'Curso de Elétrica',
            'titulo': 'Formação Profissional',
            'foto': 'projeto_eletrica.jpg',
            'responsavel': 'Rouglan',
            'situacao': 'Em breve',
            'historico': (
                'Este curso nasceu quando um adolescente chorou dizendo que '
                '"não seria nada na vida". Decidimos provar o contrário.'
            ),
            'infraestrutura': [
                'Sala para aulas práticas com bancadas de trabalho',
                'Equipamento de segurança (extintores, sinalização de segurança)',
            ],
            'materiais': [
                'Ferramentas de elétrica (multímetros, chaves de fenda, alicates, etc.)',
                'Materiais didáticos (livros, apostilas)',
                'Equipamentos de segurança (luvas, óculos, botas)',
            ],
            'objetivos': [
                'Ensinar nossos jovens uma profissão que possibilite a inserção no mercado de trabalho.',
            ],
            'destaque': '',
        },
        {
            'nome': 'Ballet na Igreja',
            'titulo': 'Arte que Transforma',
            'foto': 'projeto_ballet.jpg',
            'responsavel': 'Arina Paiva',
            'situacao': 'Em andamento',
            'historico': (
                'O ballet já mudou a autoestima de muitas meninas da igreja '
                'e do bairro. Queremos ampliar — muito.'
            ),
            'infraestrutura': [
                'Sala para aulas práticas com barras e espelhos de corpo inteiro',
                'Armários, som e iluminação',
                'Piso liso',
                'Climatização',
            ],
            'materiais': [
                'Maiôs, collants, saias e meias-calças',
                'Roupa para as aulas, como leotards, leggings e tops',
                'Sapatilhas de ballet',
            ],
            'objetivos': [
                'Chegar a 50 alunas.',
                'Criar turmas por nível.',
                'Realizar espetáculos anuais no bairro.',
            ],
            'destaque': 'Com R$100 você veste uma bailarina pela primeira vez.',
        },
    ]

    return render(request, 'projetos.html', {'projetos': lista})


# Página de doação
def doacao(request):
    return render(request, 'doacao.html')


# Cadastro de voluntários
def voluntario(request):
    erro = ''

    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        telefone = request.POST.get('telefone', '').strip()
        email = request.POST.get('email', '').strip()
        periodo = request.POST.get('periodo', '')
        projetos_escolhidos = request.POST.getlist('projetos')

        try:
            horas = int(request.POST.get('horas', '0'))
        except (ValueError, TypeError):
            horas = -1

        if not nome or not telefone or not email or not periodo:
            erro = 'Preencha todos os campos obrigatórios.'
        elif not projetos_escolhidos:
            erro = 'Selecione pelo menos um projeto.'
        elif horas < 0 or horas > 20:
            erro = 'Informe uma quantidade de horas entre 0 e 20.'
        else:
            Voluntario.objects.create(
                nome=nome,
                telefone=telefone,
                email=email,
                periodo=periodo,
                projetos=projetos_escolhidos,
                horas=horas,
            )

            return render(request, 'voluntario.html', {
                'projetos': PROJETOS_VOLUNTARIO,
                'sucesso': True,
            })

    return render(request, 'voluntario.html', {
        'projetos': PROJETOS_VOLUNTARIO,
        'erro': erro,
    })


# Login do painel administrativo
def login_admin(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('painel_admin')

    erro = False

    if request.method == 'POST':
        usuario = request.POST.get('username', '')
        senha = request.POST.get('password', '')

        usuario_autenticado = authenticate(
            request,
            username=usuario,
            password=senha,
        )

        if usuario_autenticado and usuario_autenticado.is_staff:
            login(request, usuario_autenticado)
            return redirect('painel_admin')

        erro = True

    return render(request, 'login.html', {'erro': erro})


# Painel administrativo: mostra os cadastros reais do banco
@login_required(login_url='login_admin')
def painel_admin(request):
    if not request.user.is_staff:
        logout(request)
        return redirect('login_admin')

    voluntarios = Voluntario.objects.all().order_by('-data_cadastro')

    cadastros = [
        {
            'id': v.id,
            'nome': v.nome,
            'telefone': v.telefone,
            'email': v.email,
            'periodo': v.periodo,
            'projetos': v.projetos,
            'horas': v.horas,
            'status': v.status,
            'data': v.data_cadastro,
        }
        for v in voluntarios
    ]

    por_status = {
        status: voluntarios.filter(status=status).count()
        for status in STATUS_VOLUNTARIO
    }

    ativos_por_periodo = {
        periodo: voluntarios.filter(
            status='Ativo',
            periodo=periodo,
        ).count()
        for periodo in ['Manhã', 'Tarde', 'Noite']
    }

    return render(request, 'painel.html', {
        'cadastros': cadastros,
        'ativos_por_periodo': ativos_por_periodo,
        'por_status': por_status,
        'lista_status': STATUS_VOLUNTARIO,
        'projetos': PROJETOS_VOLUNTARIO,
    })


# Atualiza o status de um voluntário
@login_required(login_url='login_admin')
def atualizar_status(request, voluntario_id):
    if not request.user.is_staff:
        logout(request)
        return redirect('login_admin')

    if request.method == 'POST':
        voluntario = get_object_or_404(Voluntario, id=voluntario_id)
        novo_status = request.POST.get('status', '')

        if novo_status in STATUS_VOLUNTARIO:
            voluntario.status = novo_status
            voluntario.save(update_fields=['status'])

    return redirect('painel_admin')


# Sai da sessão administrativa
def sair_admin(request):
    logout(request)
    return redirect('login_admin')

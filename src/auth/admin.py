from sqlalchemy.orm import Session
from src.models.usuario import Usuario
from src.models.question import Question
from src.auth.auth import get_password_hash
from src.schemas.usuario import NivelAcesso
from datetime import datetime, timezone

def criar_questoes_iniciais(db: Session):
    # Verifica se já existem questões
    questoes_existentes = db.query(Question).first()
    if questoes_existentes:
        return
    
    questoes = [
        # Aula 1
        Question(
            aula="Aula 1",
            pergunta="Por que é importante planejar antes de criar um vídeo?",
            alternativa_a="Para economizar tempo e recursos",
            alternativa_b="Para garantir qualidade de som e imagem",
            alternativa_c="Para que o vídeo tenha um propósito claro",
            alternativa_d="Todas as anteriores",
            resposta_correta="Todas as anteriores",
            data_criacao=datetime.now(timezone.utc)
        ),
        Question(
            aula="Aula 1",
            pergunta="Qual elemento é mais importante para gerar interesse no público?",
            alternativa_a="Alta resolução da câmera",
            alternativa_b="Uma história envolvente",
            alternativa_c="Efeitos visuais elaborados",
            alternativa_d="Uso de equipamentos caros",
            resposta_correta="Uma história envolvente",
            data_criacao=datetime.now(timezone.utc)
        ),
        Question(
            aula="Aula 1",
            pergunta="O que é storytelling?",
            alternativa_a="A técnica de edição de vídeos longos",
            alternativa_b="A arte de contar histórias para envolver o público",
            alternativa_c="Um tipo de equipamento de filmagem",
            alternativa_d="Uma ferramenta para ajustar o áudio de vídeos",
            resposta_correta="A arte de contar histórias para envolver o público",
            data_criacao=datetime.now(timezone.utc)
        ),
        Question(
            aula="Aula 1",
            pergunta="Qual destes NÃO é um benefício de cativar o público?",
            alternativa_a="Aumentar a audiência",
            alternativa_b="Tornar seu conteúdo mais memorável",
            alternativa_c="Tornar o vídeo mais curto",
            alternativa_d="Criar uma conexão emocional",
            resposta_correta="Tornar o vídeo mais curto",
            data_criacao=datetime.now(timezone.utc)
        ),
        Question(
            aula="Aula 1",
            pergunta="Qual é o principal objetivo ao cativar e incentivar na criação de vídeos?",
            alternativa_a="Aprender a usar ferramentas avançadas de edição",
            alternativa_b="Desenvolver habilidades técnicas em captação de som",
            alternativa_c="Inspirar criatividade e gerar conexão com o público",
            alternativa_d="Escolher o melhor equipamento para filmagem",
            resposta_correta="Inspirar criatividade e gerar conexão com o público",
            data_criacao=datetime.now(timezone.utc)
        ),
        # Aula 2
        Question(
            aula="Aula 2",
            pergunta="Qual equipamento é suficiente para começar a criar vídeos?",
            alternativa_a="Um celular com boa câmera",
            alternativa_b="Um drone",
            alternativa_c="Uma câmera DSLR de última geração",
            alternativa_d="Uma filmadora de cinema",
            resposta_correta="Um celular com boa câmera",
            data_criacao=datetime.now(timezone.utc)
        ),
        Question(
            aula="Aula 2",
            pergunta="Por que é importante testar o equipamento antes de gravar?",
            alternativa_a="Para garantir que a bateria esteja carregada",
            alternativa_b="Para se familiarizar com as funções e evitar problemas técnicos",
            alternativa_c="Para evitar gastar tempo durante a gravação",
            alternativa_d="Todas as anteriores",
            resposta_correta="Todas as anteriores",
            data_criacao=datetime.now(timezone.utc)
        ),
        Question(
            aula="Aula 2",
            pergunta="Qual é a importância de conhecer seu público antes de fazer um vídeo?",
            alternativa_a="Para escolher o equipamento certo",
            alternativa_b="Para definir o tom e estilo mais adequados",
            alternativa_c="Para ajustar a duração do vídeo",
            alternativa_d="Para economizar tempo de produção",
            resposta_correta="Para definir o tom e estilo mais adequados",
            data_criacao=datetime.now(timezone.utc)
        ),
        Question(
            aula="Aula 2",
            pergunta="Qual é o primeiro passo para começar a produzir seu vídeo?",
            alternativa_a="Escrever um roteiro detalhado",
            alternativa_b="Escolher o tema ou mensagem principal",
            alternativa_c="Aprender a editar vídeos",
            alternativa_d="Comprar uma câmera profissional",
            resposta_correta="Escolher o tema ou mensagem principal",
            data_criacao=datetime.now(timezone.utc)
        ),
        Question(
            aula="Aula 2",
            pergunta="O que é recomendado para garantir uma boa iluminação no vídeo?",
            alternativa_a="Usar luz natural ou fontes de luz estáveis",
            alternativa_b="Filmar em ambientes escuros",
            alternativa_c="Usar apenas a luz do equipamento",
            alternativa_d="Evitar iluminação direta",
            resposta_correta="Usar luz natural ou fontes de luz estáveis",
            data_criacao=datetime.now(timezone.utc)
        )
    ]
    
    for questao in questoes:
        db.add(questao)
    db.commit()
    print("Questões iniciais criadas com sucesso!")

def criar_admin_se_nao_existe(db: Session):
    # Verifica se já existe um admin
    criar_questoes_iniciais(db)
    admin = db.query(Usuario).filter(Usuario.email == "adm@adm.com").first()
    if not admin:
        # Cria o usuário admin
        admin = Usuario(
            nome="Administrador",
            email="adm@adm.com",
            senha=get_password_hash("adm"),
            nivel_acesso=NivelAcesso.ADMIN,
            data_criacao=datetime.now(timezone.utc)
        )
        db.add(admin)
        db.commit()
        db.refresh(admin)
        print("Usuário administrador criado com sucesso!")
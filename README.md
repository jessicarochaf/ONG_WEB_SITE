# Caminho da Esperança – Instituto Social

Site do projeto social **Caminho da Esperança**, da Primeira Igreja Batista em Retiro São Joaquim.
Feito com **Django** (Python), **HTML** e **CSS**.

## Páginas

- **Início** – apresentação, como ajudar e resumo dos projetos
- **Sobre** – história, pesquisa no bairro, equipe e testemunho
- **Projetos** – detalhes de cada projeto (futebol, sopão, informática, artes marciais, elétrica e ballet)
- **Doação** – PIX e contato pelo WhatsApp
- **Seja Voluntário** – formulário de inscrição (por enquanto só visual)
- **Área do administrador** (`/admin/`) – tela de login, sem link no menu
- **Painel do administrador** (`/admin/painel/`) – tabela com os cadastros de voluntários, busca e filtros por projeto e período

## Como rodar o projeto

**Precisa ter instalado:** Python 3.12 ou mais novo e Git.

1. Baixar o código:
   ```
   git clone https://github.com/leon4rdofigueiredo/ONG_WEB_SITE.git
   cd ONG_WEB_SITE
   ```

2. Criar e ativar o ambiente virtual:
   ```
   python -m venv .venv
   ```
   - Windows: `.venv\Scripts\activate`
   - Mac/Linux: `source .venv/bin/activate`

3. Instalar o Django:
   ```
   pip install django
   ```

4. Rodar o servidor:
   ```
   python manage.py runserver
   ```

5. Abrir no navegador: http://127.0.0.1:8000

> O aviso *"You have unapplied migration(s)"* pode ser ignorado, porque o site ainda não usa banco de dados.

### Login de teste

Enquanto o login de verdade não está pronto, dá para entrar no painel pela tela `/admin/` com usuário **admin** e senha **admin**.
Esse login só funciona com `DEBUG = True` (no computador de quem está desenvolvendo) e deve ser apagado quando o backend ficar pronto.

## O que já funciona

- Todas as páginas, com o mesmo menu e rodapé (`base.html`)
- Layout responsivo: no celular o menu, as caixas e a tabela do painel se reorganizam
- Busca e filtros da tabela do painel (rodam no navegador)

## O que ainda falta (backend)

- Salvar as inscrições do formulário de voluntário no banco de dados
- Login de verdade com usuários do Django (`LoginView`) no lugar do login de teste
- Proteger o painel com `@login_required` e fazer o botão **Sair** usar o logout do Django
- Trocar os cadastros de exemplo do painel pelos cadastros reais

## Estrutura

```
caminho/            configurações do Django (settings.py, urls.py)
site_ong/
  views.py          funções de cada página e textos dos projetos/equipe
  templates/        páginas HTML (base.html tem o menu e o rodapé; chamada.html é a faixa do final de Sobre e Projetos)
  static/css/       estilo do site
  static/imagens/   imagens
manage.py
```

# Caminho da Esperança – Instituto Social

Site do projeto social **Caminho da Esperança**, da Primeira Igreja Batista em Retiro São Joaquim.
Feito com **Django** (Python), **HTML** e **CSS**.

## Páginas

- **Início** – apresentação, como ajudar e resumo dos projetos
- **Sobre** – história, pesquisa no bairro, equipe e testemunho
- **Projetos** – detalhes de cada projeto (futebol, sopão, informática, artes marciais, elétrica e ballet)
- **Doação** – PIX e contato pelo WhatsApp
- **Seja Voluntário** – formulário de inscrição (por enquanto só visual)

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

## Estrutura

```
caminho/            configurações do Django (settings.py, urls.py)
site_ong/
  views.py          funções de cada página e textos dos projetos/equipe
  templates/        páginas HTML
  static/css/       estilo do site
  static/imagens/   imagens
manage.py
```

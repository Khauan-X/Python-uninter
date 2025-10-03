# 🐾 PetCare - Sistema de Agendamento para Pets

Um sistema completo de agendamento para clínicas veterinárias e pet shops, desenvolvido em Python com Flask.

## ✨ Funcionalidades

- **Agendamento Online**: Formulário completo para agendar consultas e serviços
- **Gestão de Pets**: Cadastro com informações detalhadas do pet e tutor
- **Painel Administrativo**: Controle total dos agendamentos
- **Sistema de Status**: Acompanhamento do progresso dos agendamentos
- **Verificação de Horários**: Sistema inteligente de disponibilidade
- **Interface Responsiva**: Design moderno e adaptável a todos os dispositivos

## 🚀 Como Executar

### 1. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 2. Executar a Aplicação
```bash
python app.py
```

### 3. Acessar o Sistema
- **Página Inicial**: http://localhost:5000
- **Agendamento**: http://localhost:5000/agendar
- **Administração**: http://localhost:5000/admin

## 📋 Campos do Formulário

### Dados do Tutor
- Nome completo
- Telefone

### Dados do Pet
- Nome do pet
- Idade (em anos)
- Problemas de pele (checkbox)
- Problemas genéticos (checkbox)
- Descrição detalhada dos problemas

### Agendamento
- Data
- Horário (verificação automática de disponibilidade)
- Tipo de serviço
- Observações adicionais

## 🎯 Serviços Disponíveis

- Consulta Veterinária
- Vacinação
- Banho e Tosa
- Exame de Sangue
- Cirurgia
- Tratamento de Pele
- Outros

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python + Flask
- **Banco de Dados**: SQLite + SQLAlchemy
- **Frontend**: HTML5 + CSS3 + JavaScript
- **Framework CSS**: Bootstrap 5
- **Ícones**: Font Awesome
- **Validação**: JavaScript + HTML5

## 📊 Sistema de Status

- **Pendente**: Agendamento criado, aguardando confirmação
- **Confirmado**: Agendamento confirmado pelo administrador
- **Concluído**: Serviço realizado com sucesso
- **Cancelado**: Agendamento cancelado

## 🔧 Estrutura do Projeto

```
python/
├── app.py                 # Aplicação principal Flask
├── requirements.txt       # Dependências Python
├── README.md             # Este arquivo
└── templates/            # Templates HTML
    ├── index.html        # Página inicial
    ├── agendar.html      # Formulário de agendamento
    └── admin.html        # Painel administrativo
```

## 💾 Banco de Dados

O sistema utiliza SQLite com as seguintes tabelas:

- **AgendamentoPet**: Armazena todos os dados dos agendamentos
- Campos: ID, tutor, pet, telefone, idade, problemas, data, horário, serviço, status

## 🎨 Personalização

### Cores
- **Primária**: #667eea (Azul)
- **Secundária**: #764ba2 (Roxo)
- **Sucesso**: #28a745 (Verde)
- **Aviso**: #ffc107 (Amarelo)
- **Perigo**: #dc3545 (Vermelho)

### Estilos
- Gradientes modernos
- Sombras suaves
- Animações de hover
- Design responsivo

## 📱 Responsividade

O sistema é totalmente responsivo e funciona em:
- Desktop
- Tablet
- Smartphone
- Todos os navegadores modernos

## 🔒 Segurança

- Validação de dados no frontend e backend
- Sanitização de inputs
- Proteção contra SQL injection
- Validação de datas e horários

## 🚀 Deploy

### Local
```bash
python app.py
```

### Produção
```bash
# Usar WSGI server como Gunicorn
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 📞 Suporte

Para dúvidas ou sugestões:
1. Verifique este README
2. Consulte a documentação do Flask
3. Verifique os logs da aplicação

## 🔄 Atualizações Futuras

- [ ] Sistema de usuários e login
- [ ] Notificações por email/SMS
- [ ] Relatórios e estatísticas
- [ ] API REST completa
- [ ] Integração com sistemas externos
- [ ] Backup automático do banco
- [ ] Sistema de pagamentos

## 📄 Licença

Este projeto é de uso livre para fins educacionais e comerciais.

---

**Desenvolvido com ❤️ para cuidar dos nossos amigos peludos! 🐕🐱**


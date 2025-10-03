from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agendamentos_pets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class AgendamentoPet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_tutor = db.Column(db.String(100), nullable=False)
    nome_pet = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    idade_pet = db.Column(db.Integer, nullable=False)
    problemas_pele = db.Column(db.Boolean, default=False)
    problemas_geneticos = db.Column(db.Boolean, default=False)
    descricao_problemas = db.Column(db.Text)
    data = db.Column(db.Date, nullable=False)
    horario = db.Column(db.String(10), nullable=False)
    servico = db.Column(db.String(100), nullable=False)
    observacoes = db.Column(db.Text)
    status = db.Column(db.String(20), default='pendente')
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agendar')
def agendar():
    return render_template('agendar.html')

@app.route('/admin')
def admin():
    agendamentos = AgendamentoPet.query.order_by(AgendamentoPet.data.desc()).all()
    return render_template('admin.html', agendamentos=agendamentos)

@app.route('/api/agendamentos', methods=['POST'])
def criar_agendamento():
    try:
        data = request.json
        novo_agendamento = AgendamentoPet(
            nome_tutor=data['nome_tutor'],
            nome_pet=data['nome_pet'],
            telefone=data['telefone'],
            idade_pet=int(data['idade_pet']),
            problemas_pele=data.get('problemas_pele', False),
            problemas_geneticos=data.get('problemas_geneticos', False),
            descricao_problemas=data.get('descricao_problemas', ''),
            data=datetime.strptime(data['data'], '%Y-%m-%d').date(),
            horario=data['horario'],
            servico=data['servico'],
            observacoes=data.get('observacoes', '')
        )
        db.session.add(novo_agendamento)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Agendamento criado com sucesso!'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 400

@app.route('/api/agendamentos/<int:id>/status', methods=['PUT'])
def atualizar_status(id):
    try:
        agendamento = AgendamentoPet.query.get_or_404(id)
        data = request.json
        agendamento.status = data['status']
        db.session.commit()
        return jsonify({'success': True, 'message': 'Status atualizado!'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 400

@app.route('/api/horarios-disponiveis')
def horarios_disponiveis():
    data = request.args.get('data')
    if not data:
        return jsonify({'success': False, 'message': 'Data não fornecida'})
    
    data_obj = datetime.strptime(data, '%Y-%m-%d').date()
    agendamentos_existentes = AgendamentoPet.query.filter_by(data=data_obj).all()
    horarios_ocupados = [ag.horario for ag in agendamentos_existentes]
    
    # Horários disponíveis das 8h às 18h
    todos_horarios = [f"{h:02d}:00" for h in range(8, 19)]
    horarios_disponiveis = [h for h in todos_horarios if h not in horarios_ocupados]
    
    return jsonify({'success': True, 'horarios': horarios_disponiveis})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

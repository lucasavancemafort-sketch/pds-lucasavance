from app import app, db, Dono, Pet


with app.app_context():
    db.create_all()

    # Insere exemplos somente quando o banco estiver vazio.
    if Dono.query.first() is None:
        ana = Dono(nome="Ana Paula Ribeiro", telefone="45999110001")
        bruno = Dono(nome="Bruno Cardoso", telefone="45999110002")
        carla = Dono(nome="Carla Meneghel", telefone="45999110003")

        db.session.add_all([ana, bruno, carla])
        db.session.commit()

        if Pet.query.first() is None:
            db.session.add_all([
                Pet(nome="Rex", especie="cachorro", idade=4, dono_id=ana.id),
                Pet(nome="Mimi", especie="gato", idade=2, dono_id=ana.id),
                Pet(nome="Thor", especie="cachorro", idade=7, dono_id=bruno.id),
                Pet(nome="Nina", especie="gato", idade=1, dono_id=carla.id),
                Pet(nome="Pingo", especie="passaro", idade=3, dono_id=carla.id)
            ])
            db.session.commit()

    print("Banco criado com sucesso.")

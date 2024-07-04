from django.db import connection

def create_trigger_sqlite():
    with connection.cursor() as cursor:
        #para obter um cursor sql que permite executar comando diretamento no banco de dados através do Django
        #define que a trigger será executada antes de inserir um novo registro na tabela plano_plano
        cursor.execute('''
            CREATE TRIGGER IF NOT EXISTS registra_data_criacao_trigger
            BEFORE INSERT ON plano_plano
            FOR EACH ROW
            BEGIN
                UPDATE plano_plano
                SET data_criacao = datetime('now')
                WHERE id = NEW.id;
            END;
        ''')

def listar_acoes_por_plano(plano_id):
    with connection.cursor() as cursor:
        #define uma consulta sql para listar ações por plano
        #valor do plano é passado como um parametro apos a consulta para substituir o ? na consulta
        cursor.execute("""
            SELECT *
            FROM plano_acao
            WHERE plano_id = ?;
        """, [plano_id])
        rows = cursor.fetchall() #recupera as linhas da consulta
        return rows #retorna as linhas da consulta
    
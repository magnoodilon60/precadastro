from typing import List
import services.database as db;
import models.precadmanual as precadmanual

def Incluir(precadastro):
    tb_exames = f'''INSERT INTO `complabadv`.`exames` (`NumPac`, `CodSeq`, `Exame`, `DataColeta`, `HoraColeta`, `DataEntrega`, `HoraEntrega`, `Convenio`, `Procedencia`, `TamExame`, `Faturar`, `Imprimir`, `Material`, `Digitador`, `OrdemImpressao`, `MapExtend`, `Coletar`, `DataFatura`, `Laudar`, `DataEntregaApoio`, `CodSeqIntegra`) VALUES ('{precadastro.NumPac}', '1', 'HEM', '{precadastro.DataColeta}', '{precadastro.HoraColeta}', '{precadastro.DataEntrega}', '{precadastro.HoraEntrega}', '1', '16', '0', 'S', 'S', 'N', '1', 'B001', '694', 'N', '2022-06-15', 'N', '{precadastro.DataEntregaApoio}', '0');
'''

    tb_exameaux = f'''INSERT INTO `complabadv`.`exameaux` (`NumPac`, `CodSeq`, `Exame`, `Plano`, `ConfirmResultado`, `RelacaoMedico`, `ImpFax`, `IdExame`) VALUES ('{precadastro.NumPac}', '1', 'HEM', '1', '0', '49', '32', '{precadastro.NumPac}01');
    '''

    tb_paciente = f'''INSERT INTO `complabadv`.`paciente` (`NumUnico`, `NumPac`, `RegHos`, `DataCadastro`, `HoraCadastro`, `Nome`, `Idade`, `Sexo`, `Convenio`, `Procedencia`, `Entrega`, `Internado`, `DataEntrega`, `Controle`, `IdadeReal`, `Doc` ) VALUES ('002000000006797', '{precadastro.NumPac}', '12345678901', '{precadastro.DataColeta}', '{precadastro.HoraColeta}', 'PACIENTE DE TESTE', '2000-10-10', 'F', '1', '1', '1', 'S', '{precadastro.DataEntrega}', 'N', '0210805', '12345678901');
    '''

    tb_pacaux = f'''INSERT INTO `complabadv`.`pacaux` (`NumPac`, `Plano`, `EnviaPor`, `CodInternet`) VALUES ('{precadastro.NumPac}', '1', '6', '18304');
    '''

    tb_rastretiq = f'''INSERT INTO `complabadv`.`rastretiq` (`IDAmostra`, `NumPac`, `Setor`, `Recipiente`, `Impresso`, `Situacao`, `numbancada`) VALUES ('{precadastro.NumPac}01', '{precadastro.NumPac}', '2', '1', 'S', '57', '0');
    '''
    tb_rastexames = f'''INSERT INTO `complabadv`.`rastrexames` (`IDAmostra`, `NumPac`, `CodSeq`, `Exame`) VALUES ('{precadastro.NumPac}01', '{precadastro.NumPac}', '1', 'HEM');
    '''

    tb_rastreabilidade = f'''INSERT INTO `complabadv`.`rastreabilidade` (`Sequencial`, `IDAmostra`, `Situacao`, `DataHora`,  `Operador`, `LocalRastreab`) VALUES ('403102', '{precadastro.NumPac}', '10', '{precadastro.DataEntregaApoio}', '1', '1');
    '''


    comando = [ tb_paciente, tb_exames, tb_exameaux, tb_pacaux, tb_rastretiq,tb_rastexames, tb_rastreabilidade]

    for cmd in comando:
        print(f'executando o comando {cmd}')
        db.cursor.execute(cmd)
        #sleep(2)
    #cursor.execute(tb_rastretiq)
    db.conexao.commit() # editando o banco de dados
    # resultado = cursor.fetchall() #ler o banco de dados

    #db.cursor.close()

    #db.conexao.close()


    # db.cursor.execute(f"""INSERT INTO visitante (nome, cpf, empresa, setor, DataEntrada, HoraEntrada) 
    #                   VALUES ('{preCadastroManual}', 
    #                             {visitante.cpf}, 
    #                             '{visitante.empresa}', 
    #                             '{visitante.setor}', 
    #                             '{visitante.dataentrada}', 
    #                             '{visitante.horaentrada}')"""
    #                         )
    # db.conexao.commit()
    # #db.cursor.close()


def SelecionarTodos():
    db.cursor.execute('select * from paciente')
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(precadmanual.preCadastroManual(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
    return costumerList
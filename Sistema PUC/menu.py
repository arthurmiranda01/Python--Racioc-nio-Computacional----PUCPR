import json
#Criando as funções para utilização no código
#Função Menu Principal
def display_mainMenu():
    print("Bem-Vindo ao Menu do Sistema PUC")
    print("1. Estudantes")
    print("2. Professores")
    print("3. Disciplinas")
    print("4. Turmas")
    print("5. Matrículas")
    print("0. Sair")
    return int(input("Digite uma opção válida"))

#Função Menu Secundário
def display_secondMenu():
    print("1. Criar")
    print("2. Listar")
    print("3. Atualizar")
    print("4. Excluir")
    print("0. Voltar")

#ESTUDANTES
#Função conferir o estudante
def check_student_exists(students, studentCode):
    for student in students:
        if student['Código do Estudante'] == studentCode:
            return True
    return False

#Função Criar Estudante
def creating_Student(students):
    studentName = input("Insira o nome do aluno.")
    studentCode = int(input("Insira o Código do Estudante."))
    studentDocument = int(input("Insira o CPF do Estudante."))
    
    if check_student_exists(students, studentCode):
        print("O aluno com este código já existe. Por favor, insira um novo código.")
        return False

    student_data = {
                    'Nome': studentName,
                    'Código do Estudante': int(studentCode),
                    'CPF': int(studentDocument)
                }
    students.append(student_data)
    save_archive(students, "studentsList.json")
    return True

#Função Editar Estudante
def editing_Student():
    students = read_archive("studentsList.json")
    edit_student = int(input('Digite o código do aluno que você deseja editar: '))
    editable_student = None
    for student_data in students:
        if student_data['Código do Estudante'] == edit_student:
            editable_student = student_data
            
        if editable_student == None:
                    print(f'Não encontramos estudantes com o código {edit_student} no sistema.')
        else:
                    editable_student['Nome'] = input('Digite o novo nome do Estudante: ')
                    editable_student['Código do Estudante'] = int(input('Digite o novo Código do Estudante: '))
                    editable_student['CPF'] = int(input('Digite o novo CPF do Estudante: '))
                    
    print(f'O estudante {editable_student} foi editado com sucesso.')
    save_archive(students, "studentsList.json")

#Função Listar Estudante
def listing_Student(students):
    students = read_archive("studentsList.json")
    if len(students) == 0:
        print("A lista atualmente está vazia")
    else:
        for student_name in students:
            print(f'- {student_name}')
    return students

#Função Excluir Estudante
def excluding_Student(students):
    students = read_archive("studentsList.json")
    exclude_student = int(input('Digite o código do aluno que você deseja excluir: '))
    removeble_student = None
    for student_data in students:
        if student_data['Código do Estudante'] == exclude_student:
            removeble_student = student_data
        breakpoint
        if removeble_student == None:
                    print(f'Não encontramos estudantes com o código {exclude_student} no sistema.')
        else:
                    students.remove(removeble_student)
                    print(f'O estudante {removeble_student} foi removido com sucesso.')
                    save_archive(students, "studentsList.json")
                    
#Função Criar Arquivo de Armazenamento dos ESTUDANTES
def save_archive(students, studentsList):
     with open(studentsList, 'w', encoding='utf-8') as file_opened:
          json.dump(students, file_opened, ensure_ascii=False)

#Função para ler o arquivo de armazenamento dos ESTUDANTES
def read_archive(studentsList):
    try:
        with open(studentsList, 'r', encoding='utf-8') as file_opened:
            students = json.load(file_opened)
            return students
    except Exception as e:
         print(f"Exceção ocorrida: {e}")
         return[]

#PROFESSORES
#Checkando o professor
def check_professor_exists(professors, professorCode):
    for professor in professors:
        if professor['Código do Professor'] == professorCode:
            return True
    return False

#Função para criar professores
def creating_Professor(professors):
    professorName = input("Insira o nome do Professor.")
    professorCode = int(input("Insira o Código do Professor."))
    professorDocument = int(input("Insira o CPF do Professor."))
    
    if check_professor_exists(professors, professorCode):
        print("O professor com este código já existe. Por favor, insira um novo código.")
        return False

    professor_data = {
                    'Nome': professorName,
                    'Código do Professor': int(professorCode),
                    'CPF': int(professorDocument)
                }
    professors.append(professor_data)
    save_archive(professors, "professorsList.json")
    return True

#Função para editar professores
def editing_Professor():
    professors = read_archive("professorsList.json")
    edit_professor = int(input('Digite o código do professor que você deseja editar: '))
    editable_professor = None
    for professor_data in professors:
        if professor_data['Código do Professor'] == edit_professor:
            editable_professor = professor_data
            break
    if editable_professor == None:
        print(f'Não encontramos professores com o código {edit_professor} no sistema.')
    else:
        editable_professor['Nome'] = input('Digite o novo nome para o professor: ')
        editable_professor['Código do Professor'] = int(input('Digite o novo Código do Professor: '))
        editable_professor['CPF'] = int(input('Digite o novo CPF do professor: '))
        print(f'O professor {editable_professor} foi editado com sucesso.')              

    save_archive(professors, "professorsList.json")

#Função Listar Professor
def listing_Professor(professors):
    professors = read_archive("professorsList.json")
    if len(professors) == 0:
        print("A lista atualmente está vazia")
    else:
        for professor_name in professors:
            print(f'- {professor_name}')
    return professors

#Função Excluir Professor
def excluding_Professor(professors):
    professors = read_archive("professorsList.json")
    exclude_professor = int(input('Digite o código do professor que você deseja excluir: '))
    removeble_professor = None
    for professor_data in professors:
        if professor_data['Código do Professor'] == exclude_professor:
            removeble_professor = professor_data
        breakpoint
        if removeble_professor == None:
                    print(f'Não encontramos professores com o código {exclude_professor} no sistema.')
        else:
                    professors.remove(removeble_professor)
                    print(f'O professor {removeble_professor} foi removido com sucesso.')
                    save_archive(professors, "professorsList.json")

#Função Criar Arquivo de Armazenamento dos PROFESSORES
def save_archive(professors, professorsList):
     with open(professorsList, 'w', encoding='utf-8') as file_opened:
          json.dump(professors, file_opened, ensure_ascii=False)

#Função para ler o arquivo de armazenamento dos PROFESSORES
def read_archive(professorsList):
    try:
        with open(professorsList, 'r', encoding='utf-8') as file_opened:
            professors = json.load(file_opened)
            return professors
    except Exception as e:
         print(f"Exceção ocorrida: {e}")
         return[]

#DISCIPLINAS
#Checkando a disponibilidade da disciplina
def check_subject_exists(subjects, subjectCode):
    for subject in subjects:
        if subject['Código da Disciplina'] == subjectCode:
            return True
    return False

#Função para criar disciplinas
def creating_Subject(subjects):
    subjectName = input("Insira o nome da Disciplina.")
    subjectCode = int(input("Insira o Código da Disciplina."))
    
    if check_subject_exists(subjects, subjectCode):
        print("A disciplina com este código já existe. Por favor, insira um novo código.")
        return False

    subject_data = {
                    'Nome': subjectName,
                    'Código da Disciplina': int(subjectCode),
                }
    subjects.append(subject_data)
    save_archive(subjects, "subjectsList.json")
    return True

#Função para editar as disciplinas
def editing_Subject():
    subjects = read_archive("subjectsList.json")
    edit_subjects = int(input('Digite o código da disciplina que você deseja editar: '))
    editable_subject = None
    for subject_data in subjects:
        if subject_data['Código da Disciplina'] == edit_subjects:
            editable_subject = subject_data
            break
    if editable_subject == None:
        print(f'Não encontramos disciplinas com o código {edit_subjects} no sistema.')
    else:
        editable_subject['Nome'] = input('Digite o novo nome para a Disciplina: ')
        editable_subject['Código da Disciplina'] = int(input('Digite o novo Código da Disciplina: '))
        print(f'A disciplina {editable_subject} foi editado com sucesso.')              

    save_archive(subjects, "subjectsList.json")

#Função Listar Disciplina
def listing_Subject(subjects):
    subjects = read_archive("subjectsList.json")
    if len(subjects) == 0:
        print("A lista atualmente está vazia")
    else:
        for subject_name in subjects:
            print(f'- {subject_name}')
    return subjects

#Função Excluir Disciplina
def excluding_Subject(subjects):
    subjects = read_archive("subjectsList.json")
    exclude_subject = int(input('Digite o código da disciplina que você deseja excluir: '))
    removeble_subject = None
    for subject_data in subjects:
        if subject_data['Código da Disciplina'] == exclude_subject:
            removeble_subject = subject_data
        breakpoint
        if removeble_subject == None:
                    print(f'Não encontramos disciplinas com o código {exclude_subject} no sistema.')
        else:
                    subjects.remove(removeble_subject)
                    print(f'A disciplina {removeble_subject} foi removido com sucesso.')
                    save_archive(subjects, "subjectsList.json")

#Função Criar Arquivo de Armazenamento das DISCIPLINAS
def save_archive(subjects, subjectsList):
     with open(subjectsList, 'w', encoding='utf-8') as file_opened:
          json.dump(subjects, file_opened, ensure_ascii=False)

#Função para ler o arquivo de armazenamento dos DISCIPLINAS
def read_archive(subjectsList):
    try:
        with open(subjectsList, 'r', encoding='utf-8') as file_opened:
            subjects = json.load(file_opened)
            return subjects
    except Exception as e:
         print(f"Exceção ocorrida: {e}")
         return[]

#TURMAS
#Verificando disponibilidade de turmas
def check_class_exists(classes, classCode):
    for class_data in classes:
        if class_data['Código da Turma'] == classCode:
            return True
    return False

#Função para criar Turmas
def creating_Class(classes):
    classCode = int(input("Insira o código da turma."))
    classProfessorCode = int(input("Insira o código do professor da turma."))
    classSubjectCode = int(input("Insira o código da disciplina da turma."))
    
    if check_class_exists(classes, classCode):
        print("A turma com este código já existe. Por favor, insira um novo código.")
        return False

    class_data = {
                    'Código da Turma': int(classCode),
                    'Código do Professor da Turma': int(classProfessorCode),
                    'Código da Disciplina da Turma': int(classSubjectCode)
                }
    classes.append(class_data)
    save_archive(classes, "classesList.json")
    return True

#Função para editar as turmas
def editing_Class():
    classes = read_archive("classesList.json")
    edit_classes = int(input('Digite o código da turma que você deseja editar: '))
    editable_class = None
    for class_data in classes:
        if class_data['Código da Turma'] == edit_classes:
            editable_class = class_data
            break
    if editable_class == None:
        print(f'Não encontramos turmas com o código {edit_classes} no sistema.')
    else:
        editable_class['Código da Turma'] = int(input('Digite o novo código para a turma: '))
        editable_class['Código do Professor da Turma'] = int(input('Digite o novo Código do Professor da Turma: '))
        editable_class['Código da Disciplina da Turma'] = int(input('Digite o novo Código da Disciplina da Turma: '))
        print(f'A turma {editable_class} foi editada com sucesso.')              

    save_archive(classes, "classesList.json")

#Função Listar Turmas
def listing_Class(classes):
    classes = read_archive("classesList.json")
    if len(classes) == 0:
        print("A lista atualmente está vazia")
    else:
        for class_name in classes:
            print(f'- {class_name}')
    return classes

#Função Excluir Turmas
def excluding_Class(classes):
    classes = read_archive("classesList.json")
    exclude_class = int(input('Digite o código da turma que você deseja excluir: '))
    removeble_class = None
    for class_data in classes:
        if class_data['Código da Turma'] == exclude_class:
            removeble_class = class_data
        breakpoint
        if removeble_class == None:
            print(f'Não encontramos turmas com o código {exclude_class} no sistema.')
        else:
            classes.remove(removeble_class)
            print(f'A turma {removeble_class} foi removido com sucesso.')
            save_archive(classes, "classesList.json")

#Função Criar Arquivo de Armazenamento das TURMAS
def save_archive(classes, classesList):
     with open(classesList, 'w', encoding='utf-8') as file_opened:
          json.dump(classes, file_opened, ensure_ascii=False)

#Função para ler o arquivo de armazenamento dos TURMAS
def read_archive(classesList):
    try:
        with open(classesList, 'r', encoding='utf-8') as file_opened:
            classes = json.load(file_opened)
            return classes
    except Exception as e:
         print(f"Exceção ocorrida: {e}")
         return[]

#MATRÍCULAS
#Verificando a disponibilidade da matrícula
def check_enrollment_exists(enrollments, enrollmentClassCode, enrollmentStudentCode):
    for enrollment in enrollments:
        if enrollment['Código da Turma'] == enrollmentClassCode and enrollment['Código do Estudante'] == enrollmentStudentCode:
            return True
    return False

#Função para criar uma matrícula.
def creating_Enrollments(enrollments):
    enrollmentClassCode = int(input("Insira o código da turma."))
    enrollmentStudentCode = int(input("Insira o código do estudante."))
    
    if check_enrollment_exists(enrollments, enrollmentClassCode, enrollmentStudentCode):
        print("A matrícula com este código de turma e código de estudante já existe. Por favor, insira novos códigos.")
        return False

    enrollment_data = {
                    'Código da Turma': int(enrollmentClassCode),
                    'Código do Estudante': int(enrollmentStudentCode),
                }
    enrollments.append(enrollment_data)
    save_archive(enrollments, "enrollmentsList.json")
    return True

#Função para editar as matrículas
def editing_Enrollment():
    enrollments = read_archive("enrollmentsList.json")
    edit_enrollments = int(input('Digite o código da matrícula que você deseja editar: '))
    editable_enrollment = None
    for enrollment_data in enrollments:
        if enrollment_data['Código da Turma'] == edit_enrollments:
            editable_enrollment = enrollment_data
            break
    if editable_enrollment == None:
        print(f'Não encontramos matrículas com o código {edit_enrollments} no sistema.')
    else:
        editable_enrollment['Código da Turma'] = int(input('Digite o novo código de turma para a matrícula: '))
        editable_enrollment['Código do Estudante'] = int(input('Digite o novo Código do Estudante para a matrícula: '))
        print(f'A matrícula {editable_enrollment} foi editada com sucesso.')              

    save_archive(enrollments, "enrollmentsList.json")

#Função Listar Matrículas
def listing_Enrollment(enrollments):
    enrollments = read_archive("enrollmentsList.json")
    if len(enrollments) == 0:
        print("A lista atualmente está vazia")
    else:
        for enrollment_name in enrollments:
            print(f'- {enrollment_name}')
    return enrollments

#Função Excluir Matrículas
def excluding_Enrollment(enrollments):
    enrollments = read_archive("enrollmentsList.json")
    exclude_enrollment = int(input('Digite o código do estudante que você deseja excluir uma matrícula: '))
    removeble_enrollment = None
    for enrollment_data in enrollments:
        if enrollment_data['Código do Estudante'] == exclude_enrollment:
            removeble_enrollment = enrollment_data
        breakpoint
        if removeble_enrollment == None:
            print(f'Não encontramos matrículas com o código {exclude_enrollment} no sistema.')
        else:
            enrollments.remove(removeble_enrollment)
            print(f'A matrícula {removeble_enrollment} foi removido com sucesso.')
            save_archive(enrollments, "enrollmentsList.json")

#Função Criar Arquivo de Armazenamento das Matrículas
def save_archive(enrollments, enrollmentsList):
     with open(enrollmentsList, 'w', encoding='utf-8') as file_opened:
          json.dump(enrollments, file_opened, ensure_ascii=False)

#Função para ler o arquivo de armazenamento dos Matrículas
def read_archive(enrollmentsList):
    try:
        with open(enrollmentsList, 'r', encoding='utf-8') as file_opened:
            enrollments = json.load(file_opened)
            return enrollments
    except Exception as e:
         print(f"Exceção ocorrida: {e}")
         return[]

#Criando a lista para armazenar os Estudantes
students = []
#Criando a lista para armazenar os Professores
professors = []
#Criando a lista para armazenar as Disciplinas
subjects = []
#Criando a lista para armazenar as Turmas
classes = []
#Criando a lista para armazenar as Matrículas
enrollments = []

#Variáveis das respostas do primeiro menu
student_option = ("Estudantes")
professor_option = ("Professores")
subject_option = ("Disciplinas")
class_option = ("Turmas")
enrollment_option = ("Matrículas")
exit_option = ("Sair")

#Variáveis das respostas do segundo menu
create_option = ("Criar")
list_option = ("Listar")
att_option = ("Atualizar")
excl_option = ("Excluir")

while True:
    # Mostrando o menu principal do sistema.
    option = display_mainMenu()

    if option == 1:
        print(f"Você escolheu a opção válida: {option}")

        #Mostrando o menu de operações da opção escolhida
        while True:
            if option == 1:
                print(f"Menu de Operações - Opção: {student_option}")
                display_secondMenu()
            
            elif option == 2:
                print(f"Menu de Operações - Opção: {professor_option}")
                display_secondMenu()

            elif option == 3:
                print(f"Menu de Operações - Opção: {subject_option}")
                display_secondMenu()
                
            elif option == 4:
                print(f"Menu de Operações - Opção: {class_option}")
                display_secondMenu()
                
            elif option == 5:
                print(f"Menu de Operações - Opção: {enrollment_option}")
                display_secondMenu()
                

            #Coletando a resposta do segundo menu
            second_option = int(input("Digite uma opção válida"))
            #Opção ESTUDANTES
            if second_option == 1:
                print(f"Você escolheu a opção válida: {second_option} - {create_option}")
                if creating_Student(students):
                    print(f"Você adicionou corretamente o aluno {students[-1]['Nome']} para a lista")

            elif second_option == 2:
                print(f"Você escolheu a opção válida: {second_option} - {list_option}")
                #Listando os alunos, caso a lista esteja vazia, o sistema informará.
                listing_Student(students)
            
            #Editando o estudante
            elif second_option == 3:
                print(f"Você escolheu a opção válida: {second_option} - {att_option}")
                editing_Student()
                
                #Excluindo um aluno da lista
            elif second_option == 4:
                print(f"Você escolheu a opção válida: {second_option} - {excl_option}")
                student_data = excluding_Student(students)

            elif second_option == 0:
                print("Você pediu para voltar.")  
                break
            else: 
                print(f"Você escolheu uma alternativa incorreta: {second_option}")

    elif option == 0:
            print("Você pediu para sair.")
            break
    
    elif option == 2: #Professores
            print(f"Você escolheu a opção válida: {option}")
            #Mostrando o menu de operações da opção escolhida
            while True:
                if option == 1:
                    print(f"Menu de Operações - Opção: {student_option}")
                    display_secondMenu()
            
                elif option == 2:
                    print(f"Menu de Operações - Opção: {professor_option}")
                    display_secondMenu()

                elif option == 3:
                    print(f"Menu de Operações - Opção: {subject_option}")
                    display_secondMenu()
                
                elif option == 4:
                    print(f"Menu de Operações - Opção: {class_option}")
                    display_secondMenu()
                
                elif option == 5:
                    print(f"Menu de Operações - Opção: {enrollment_option}")
                    display_secondMenu()
                
                #Coletando a resposta do segundo menu
                second_option = int(input("Digite uma opção válida"))
                #Opção PROFESSORES
                if second_option == 1:
                    print(f"Você escolheu a opção válida: {second_option} - {create_option}")
                    if creating_Professor(professors):
                        print(f"Você adicionou corretamente o professor {professors[-1]['Nome']} para a lista")

                elif second_option == 2:
                    print(f"Você escolheu a opção válida: {second_option} - {list_option}")
                    #Listando os professores, caso a lista esteja vazia, o sistema informará.
                    listing_Professor(professors)
            
                #Editando o professor
                elif second_option == 3:
                    print(f"Você escolheu a opção válida: {second_option} - {att_option}")
                    editing_Professor()
                
                #Excluindo um professor da lista
                elif second_option == 4:
                    print(f"Você escolheu a opção válida: {second_option} - {excl_option}")
                    professor_data = excluding_Professor(professors)

                elif second_option == 0:
                    print("Você pediu para voltar.")  
                    break
                else: 
                    print(f"Você escolheu uma alternativa incorreta: {second_option}")
    
    elif option == 3: #Disciplinas
            print(f"Você escolheu a opção válida: {option}")
            #Mostrando o menu de operações da opção escolhida
            while True:
                if option == 1:
                    print(f"Menu de Operações - Opção: {student_option}")
                    display_secondMenu()
            
                elif option == 2:
                    print(f"Menu de Operações - Opção: {professor_option}")
                    display_secondMenu()

                elif option == 3:
                    print(f"Menu de Operações - Opção: {subject_option}")
                    display_secondMenu()
                
                elif option == 4:
                    print(f"Menu de Operações - Opção: {class_option}")
                    display_secondMenu()
                
                elif option == 5:
                    print(f"Menu de Operações - Opção: {enrollment_option}")
                    display_secondMenu()
                
                #Coletando a resposta do segundo menu
                second_option = int(input("Digite uma opção válida"))
                #Opção DISCIPLINAS
                if second_option == 1:
                    print(f"Você escolheu a opção válida: {second_option} - {create_option}")
                    if creating_Subject(subjects):
                        print(f"Você adicionou corretamente a disciplina {subjects[-1]['Nome']} para a lista")

                elif second_option == 2:
                    print(f"Você escolheu a opção válida: {second_option} - {list_option}")
                    #Listando as disciplinas, caso a lista esteja vazia, o sistema informará.
                    listing_Subject(subjects)
            
                #Editando a disciplina
                elif second_option == 3:
                    print(f"Você escolheu a opção válida: {second_option} - {att_option}")
                    editing_Subject()
                
                #Excluindo uma disciplina da lista
                elif second_option == 4:
                    print(f"Você escolheu a opção válida: {second_option} - {excl_option}")
                    subject_data = excluding_Subject(subjects)

                elif second_option == 0:
                    print("Você pediu para voltar.")  
                    break
                else: 
                    print(f"Você escolheu uma alternativa incorreta: {second_option}")
    
    elif option == 4: #Turmas
            print(f"Você escolheu a opção válida: {option}")
            #Mostrando o menu de operações da opção escolhida
            while True:
                if option == 1:
                    print(f"Menu de Operações - Opção: {student_option}")
                    display_secondMenu()
            
                elif option == 2:
                    print(f"Menu de Operações - Opção: {professor_option}")
                    display_secondMenu()

                elif option == 3:
                    print(f"Menu de Operações - Opção: {subject_option}")
                    display_secondMenu()
                
                elif option == 4:
                    print(f"Menu de Operações - Opção: {class_option}")
                    display_secondMenu()
                
                elif option == 5:
                    print(f"Menu de Operações - Opção: {enrollment_option}")
                    display_secondMenu()
                
                #Coletando a resposta do segundo menu
                second_option = int(input("Digite uma opção válida"))
                #Opção TURMAS
                if second_option == 1:
                    print(f"Você escolheu a opção válida: {second_option} - {create_option}")
                    if creating_Class(classes):
                        print(f"Você adicionou corretamente a turma {classes[-1]['Código da Turma']} para a lista")

                elif second_option == 2:
                    print(f"Você escolheu a opção válida: {second_option} - {list_option}")
                    #Listando as turmas, caso a lista esteja vazia, o sistema informará.
                    listing_Class(classes)
            
                #Editando a turma
                elif second_option == 3:
                    print(f"Você escolheu a opção válida: {second_option} - {att_option}")
                    editing_Class()
                
                #Excluindo uma turma da lista
                elif second_option == 4:
                    print(f"Você escolheu a opção válida: {second_option} - {excl_option}")
                    class_data = excluding_Class(classes)

                elif second_option == 0:
                    print("Você pediu para voltar.")  
                    break
                else: 
                    print(f"Você escolheu uma alternativa incorreta: {second_option}")

    elif option == 5: #Matrículas
            print(f"Você escolheu a opção válida: {option}")
            #Mostrando o menu de operações da opção escolhida
            while True:
                if option == 1:
                    print(f"Menu de Operações - Opção: {student_option}")
                    display_secondMenu()
            
                elif option == 2:
                    print(f"Menu de Operações - Opção: {professor_option}")
                    display_secondMenu()

                elif option == 3:
                    print(f"Menu de Operações - Opção: {subject_option}")
                    display_secondMenu()
                
                elif option == 4:
                    print(f"Menu de Operações - Opção: {class_option}")
                    display_secondMenu()
                
                elif option == 5:
                    print(f"Menu de Operações - Opção: {enrollment_option}")
                    display_secondMenu()
                
                #Coletando a resposta do segundo menu
                second_option = int(input("Digite uma opção válida"))
                #Opção MATRÍCULAS
                if second_option == 1:
                    print(f"Você escolheu a opção válida: {second_option} - {create_option}")
                    if creating_Enrollments(enrollments):
                        print(f"Você adicionou corretamente a matrícula {enrollments[-1]['Código do Estudante']} para a lista")

                elif second_option == 2:
                    print(f"Você escolheu a opção válida: {second_option} - {list_option}")
                    #Listando as matrículas, caso a lista esteja vazia, o sistema informará.
                    listing_Enrollment(enrollments)
            
                #Editando a matrícula
                elif second_option == 3:
                    print(f"Você escolheu a opção válida: {second_option} - {att_option}")
                    editing_Enrollment()
                
                #Excluindo uma matrícula da lista
                elif second_option == 4:
                    print(f"Você escolheu a opção válida: {second_option} - {excl_option}")
                    enrollment_data = excluding_Enrollment(enrollments)

                elif second_option == 0:
                    print("Você pediu para voltar.")  
                    break
                else: 
                    print(f"Você escolheu uma alternativa incorreta: {second_option}")
    else:
        print(f"Você escolheu uma alternativa incorreta: {option}")     
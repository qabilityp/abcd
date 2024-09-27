class CounterError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class Human:

    def __init__(self, gender: str, age: int, first_name: str, last_name: str):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        pass

    def __str__(self) -> str:
        return f'gender: {self.gender}, age: {self.age}, first_name: {self.first_name}, last_name: {self.last_name}'
        pass


class Student(Human):

    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book
        pass

    def __str__(self) -> str:
        return (f'gender: {self.gender}, age: {self.age}, first_name: {self.first_name}, last_name: {self.last_name}, '
                f'record_book: {self.record_book}')
        pass

    def __eq__(self, other) -> bool:
        if isinstance(other, Student):
            return self.__str__() == other.__str__()
        return False

    def __hash__(self) -> int:
        return hash(str(self))


class Group:

    def __init__(self, number: str):
        self.number = number
        self.group = set()

    def add_student(self, student) -> None:
        if len(self.group) > 10:
            raise CounterError('Занадто багато студентів у групі')
        self.group.add(student)

    def delete_student(self, last_name: str) -> Student | None:
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)
            return student
        return None
        pass

    def find_student(self, last_name: str) -> Student | None:
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None
        pass

    def __str__(self) -> str:
        all_students = '\n'.join([str(student) for student in self.group])
        return f'Number:{self.number}\n {all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr)  # Only one student

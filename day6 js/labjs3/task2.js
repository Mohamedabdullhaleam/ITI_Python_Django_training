
var students = [
    { firstName: 'Ali', age: 22, grade: 100 },
    { firstName: 'Nora', age: 20, grade: 90 },
    { firstName: 'Nada', age: 25, grade: 75 },
    { firstName: 'Heba', age: 19, grade: 50 },
    { firstName: 'Bassem', age: 21, grade: 40 }
];

students.forEach(displayStudentInfo);
document.write(`<h2 style="color: red;">Students with Grades Greater than 80</h2>`);

students.filter(student => student.grade > 80).forEach(displayStudentInfo);

document.write(`<h2 style="color: red;">Students Names Ordered Ascendingly</h2>`);

students.sort((a, b) => a.firstName.localeCompare(b.firstName)).forEach(displayStudentInfo);


function displayStudentInfo(student) {
    document.write(`<h2>${student.firstName}: ${student.age}: ${student.grade}</h2>`);
}

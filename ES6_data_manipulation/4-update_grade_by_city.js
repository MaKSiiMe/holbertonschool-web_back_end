export default function updateStudentGradeByCity(students, city, newGrades) {
  if (!Array.isArray(students)) return [];
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const gradeEntry = newGrades.find((entry) => entry.studentId === student.id);
      return { ...student, grade: gradeEntry ? gradeEntry.grade : 'N/A' };
    });
}
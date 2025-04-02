export default function getStudentIdsSum(students) {
  return students.reduce((sum, val) => sum + val.id, 0);
}
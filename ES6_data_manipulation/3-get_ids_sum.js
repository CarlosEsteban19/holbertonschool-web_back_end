export default function getStudentIdsSum(list) {
  return list.reduce((sum, index) => sum + index.id, 0);
}

export default function getStudentIdsSum(list) {
  const initialValue = 0;
  const sum = list.reduce((accumulator, currentValue) => accumulator + currentValue, initialValue);
  return sum;
}

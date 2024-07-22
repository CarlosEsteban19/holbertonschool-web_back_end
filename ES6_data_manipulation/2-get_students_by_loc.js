export default function getStudentsByLocation(list, city) {
  return list.filter((index) => index.location === city);
}

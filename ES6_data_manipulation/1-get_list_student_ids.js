export default function getListStudentIds(array) {
    if (typeof array != Array)
        return []
    return array.map((index) => index.id);
}

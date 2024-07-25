export default function divideFunction(numerator, denominator) {
  return new Promise((resolve, reject) => {
    try {
      resolve(numerator / denominator);
    } catch (error) {
      reject(new Error('cannot divide by 0'));
    }
  });
}

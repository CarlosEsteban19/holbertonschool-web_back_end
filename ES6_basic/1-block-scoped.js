export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    /* eslint-disable */
    const task = true;
    const task2 = false;
	/* eslint-enable */
  }

  return [task, task2];
}

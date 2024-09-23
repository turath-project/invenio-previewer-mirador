import { MiradorPreviewer } from './MiradorPreviewer';

export const customPreviewers = [
  {
    name: 'MiradorPreviewer',
    component: MiradorPreviewer,
    fileTypes: ['application/json'],
    canPreview: (file) => {
      return file.key.endsWith('.json');
    },
  },
];

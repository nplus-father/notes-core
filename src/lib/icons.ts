export const icons = {
  guide:
    '<path d="M12 6.6C10.2 5.3 7.8 4.6 4 4.6v13.2c3.8 0 6.2.7 8 2 1.8-1.3 4.2-2 8-2V4.6c-3.8 0-6.2.7-8 2Z"/><path d="M12 6.6v13.2"/>',
  concepts:
    '<circle cx="6" cy="7" r="2.25"/><circle cx="18" cy="7" r="2.25"/><circle cx="12" cy="17" r="2.25"/><path d="M8.25 7h7.5M7.16 8.93l3.68 6.14M16.84 8.93l-3.68 6.14"/>',
  problems:
    '<path d="M6 3.75h8.5l3.5 3.5v13H6Z"/><path d="M14.5 3.75v3.5H18M9 11.5h6M9 15h6M9 18.5h3.5"/>',
  check: '<path d="M4.75 4.75h14.5v14.5H4.75Z"/><path d="m8.5 12.25 2.4 2.4 4.6-5"/>',
  search: '<circle cx="10.5" cy="10.5" r="6"/><path d="m15 15 5 5"/>',
  library:
    '<path d="M3.75 20.25h16.5M5.5 20.25V5h3v15.25M10.5 20.25V7.5h3v12.75"/><path d="m15.2 8.4 2.9-.78 3.25 12.1-2.9.78Z"/>',
  handbook:
    '<path d="M6.25 4h12v14.25h-12a1.75 1.75 0 0 0-1.75 1.75V5.75C4.5 4.78 5.28 4 6.25 4Z"/><path d="M4.5 20c0-.97.78-1.75 1.75-1.75h12V20.5H6.25M9.25 4v6.25l1.75-1.25 1.75 1.25V4"/>',
  archive: '<path d="M4.75 4.25h14.5v15.5H4.75ZM4.75 12h14.5"/><path d="M10 8.1h4M10 15.9h4"/>',
  bookmark: '<path d="M7 4.25h10v15.5l-5-3.5-5 3.5Z"/>',
  "arrow-left": '<path d="M19 12H5M10.5 6.5 5 12l5.5 5.5"/>',
  "arrow-right": '<path d="M5 12h14M13.5 6.5 19 12l-5.5 5.5"/>',
  "arrow-up-right": '<path d="M7.5 16.5 16.5 7.5M9 7.5h7.5V15"/>',
  "chevron-left": '<path d="M14.5 6 8.5 12l6 6"/>',
  "chevron-right": '<path d="m9.5 6 6 6-6 6"/>',
  sun: '<circle cx="12" cy="12" r="3.75"/><path d="M12 2.75v2M12 19.25v2M2.75 12h2M19.25 12h2M5.46 5.46l1.41 1.41M17.13 17.13l1.41 1.41M18.54 5.46l-1.41 1.41M6.87 17.13l-1.41 1.41"/>',
  moon: '<path d="M19.5 14.6A7.75 7.75 0 0 1 9.4 4.5a7.75 7.75 0 1 0 10.1 10.1Z"/>',
  checkup: '<path d="M3 12.5h4l2.25-5.5 4.5 11 2.25-5.5H21"/>',
  enrich: '<path d="m14.75 4.75 4.5 4.5L9 19.5H4.5V15Z"/><path d="m12.5 7 4.5 4.5"/>',
  plus: '<path d="M12 5v14M5 12h14"/>',
  minus: '<path d="M5 12h14"/>',
  copy: '<path d="M8.75 8.75h10.5v10.5H8.75Z"/><path d="M15.25 8.75v-4H4.75v10.5h4"/>',
  close: '<path d="m6 6 12 12M18 6 6 18"/>',
} as const;

export type IconName = keyof typeof icons;

export function isIconName(name: string): name is IconName {
  return Object.prototype.hasOwnProperty.call(icons, name);
}

import { TestBed } from '@angular/core/testing';

import { MintedByService } from './minted-by.service';

describe('MintedByService', () => {
  let service: MintedByService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(MintedByService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});

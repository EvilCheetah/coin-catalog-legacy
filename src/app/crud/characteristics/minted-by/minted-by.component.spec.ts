import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MintedByComponent } from './minted-by.component';

describe('MintedByComponent', () => {
  let component: MintedByComponent;
  let fixture: ComponentFixture<MintedByComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MintedByComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MintedByComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

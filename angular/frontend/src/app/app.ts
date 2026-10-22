import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  imports: [CommonModule, FormsModule],
  selector: 'app-root',
  styleUrl: './app.scss',
  templateUrl: './app.html',
})
export class App {
  protected readonly title = 'Control de attendance · MVP';
  protected username = 'admin';
  protected userpassword = '1234';

  protected loginOk = false;
  protected loginMessage = '';
  protected loading = false;

  protected resumen: {
    titulo: string;
    total_personas: number;
    attendances_hoy: number;
    actividad_activa: string;
    actualizado_en: string;
  } | null = null;

  constructor(private readonly http: HttpClient) {}

  protected login(): void {
    this.loading = true;
    this.loginMessage = '';

    this.http
      .post<{ ok: boolean; mensaje: string }>('/api/login', {
        username: this.username,
        userpassword: this.userpassword,
      })
      .subscribe({
        next: (response) => {
          this.loginOk = response.ok;
          this.loginMessage = response.mensaje;
          this.loading = false;
          if (response.ok) {
            this.loadResumen();
          } else {
            this.resumen = null;
          }
        },
        error: () => {
          this.loading = false;
          this.loginOk = false;
          this.resumen = null;
          this.loginMessage = 'No se pudo conectar con el backend.';
        },
      });
  }

  protected loadResumen(): void {
    this.http
      .get<{
        titulo: string;
        total_personas: number;
        attendances_hoy: number;
        actividad_activa: string;
        actualizado_en: string;
      }>('/api/mvp/resumen')
      .subscribe({
        next: (data) => {
          this.resumen = data;
        },
        error: () => {
          this.resumen = null;
          this.loginMessage = 'Login correcto, pero no se pudo cargar el resumen.';
        },
      });
  }
}

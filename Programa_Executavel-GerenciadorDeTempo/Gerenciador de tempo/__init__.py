from tkinter import *
from time import sleep
from bibliotecas.add import add
from datetime import datetime
import winsound
import os

def program(window, a, s, active, reset, res):
    global r_cont;global cr_active;global cr_cont;global n_show;global cont;global var_scale
    global e;global mode;global menubar;global alarmes;global add_alarm;global palet_color;global cont_prefs
    cont, alarmes = 0, []
    r_cont, cr_cont, cont_prefs = 0, 0, 0
    cr_active = True
    var = IntVar()
    palet_color = [{'BG':'#000000', 'FG':'#0dff00', 'AC_FG':'#94ff88'}, {'BG':'#ffffff', 'FG':'#000000', 'AC_FG':'#323232'}]
    e = 32

    def resource_path(relative_path):
    # Get absolute path to resource, works for dev and for PyInstaller
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def relogio():
        global r_cont;global h;global format_hora
        global cr_active;global mode;global alarmes

        cr_active = False
        r_cont += 1
        if r_cont >= 2:
            h.destroy()

        text.destroy()
        b_start.destroy()
        b_stop.destroy()
        b_reset.destroy()

        # window.iconbitmap(resource_path('media/icons/icons/main.ico'))
        window.iconbitmap('C:\\Users\\Paulo Thiago\\Downloads\\scripts\\python_curso_em_video\\Exercicios e Ideias\\Exercicios extras\\cronometro\\media\\icons\\icons\\main.ico')
        window.update_idletasks()
        while True:
            format_hora = datetime.now().strftime('%H:%M:%S')
            h = Label(window, text = format_hora, 
                      font = ('LCDMono2', (e + 60), 'bold'), 
                      bg = palet_color[0]['BG'], fg = palet_color[0]['FG'])
            h.pack(expand = True, anchor = CENTER)
            window.update()
            h.destroy()
            for c in alarmes:
                print(c['hora'])
                if c['hora'] == datetime.now().strftime('%H:%M'):
                    for alr in range(0, 3):
                        print('ALARMANDO!', end = ' ', flush = True)
                        sleep(0.3)

            if cr_active == True:
                break
        else:
            h.destroy()
            print(type(h), bool(h))

    def prefs():
        global cont_prefs;global p;global white;global black;global bt_ok

        cont_prefs += 1
        # prefs_icon = PhotoImage(file = 'C:/Users/Paulo Thiago/Downloads/scripts/python_curso_em_video/Exercicios e Ideias/Exercicios extras/cronometro/media/icons/prefs.png')

        p = Toplevel(window)
        p['bg'] = palet_color[0]['BG']
        p.title('Preferências')
        p.geometry('400x350+540+210')
        p.resizable(0, 0)
        p.grab_set()
        # p.iconbitmap(resource_path('media/icons/icons/prefs.ico'))
        p.iconbitmap('C:\\Users\\Paulo Thiago\\Downloads\\scripts\\python_curso_em_video\\Exercicios e Ideias\\Exercicios extras\\cronometro\\media\\icons\\icons\\prefs.ico')
        # p.iconphoto(False, prefs_icon)

        def rel1():
            if cr_active == False:
                relogio()
            else:
                cron()

        def sair():
            rel1()
            p.destroy()

        def interface(value):
            global p;global white;global black;global bt_ok;global p_msg
            p.config(bg = palet_color[value]['BG'])

            p_msg = Label(p, text = 'OBS. ESTA AREA AINDA NAO ESTA DISPONIVEL \nPOIS ESTA SENDO DESENVOLVIDA', 
                          font = ('LCDMono2', 13), bg = palet_color[0]['BG'], fg = palet_color[0]['FG'])
            p_msg.pack(side = TOP, anchor = NW, fill = X)

            white = Radiobutton(p, text = 'Tema claro', variable = var, value = 1, command = None, bg = palet_color[value]['BG'], 
                                fg = palet_color[value]['FG'], activebackground = palet_color[value]['BG'], 
                                activeforeground = palet_color[value]['AC_FG'], state = DISABLED)
            white.pack(side = TOP, anchor = W, fill = X)

            black = Radiobutton(p, text = 'Tema escuro', variable = var, value = 2, command = None, bg = palet_color[value]['BG'], 
                                fg = palet_color[value]['FG'], activebackground = palet_color[value]['BG'], 
                                activeforeground = palet_color[value]['AC_FG'], state = DISABLED)
            black.pack(side = TOP, anchor = W, fill = X)

            bt_ok = Button(p, text = 'Ok', bg = palet_color[value]['BG'], fg = palet_color[value]['FG'], width = 10, bd = .5, 
            command = sair, activebackground = palet_color[value]['BG'], activeforeground = palet_color[value]['AC_FG'])
            
            bt_ok.pack(side = BOTTOM, anchor = SE)

        # def sel():
        #     window.config(bg = palet_color[var.get() - 1]['BG'])
            
        #     h.config(bg = palet_color[var.get() - 1]['BG'], fg = palet_color[var.get() - 1]['FG'])

        #     tit.config(bg = palet_color[var.get() - 1]['BG'], fg = palet_color[var.get() - 1]['FG'], 
        #                selectbackground = palet_color[var.get() - 1]['FG'], 
        #                selectforeground = palet_color[var.get() - 1]['BG'], 
        #                insertbackground = palet_color[var.get() - 1]['FG'])

        # if cont == 1:
        #     interface(0)
        #     black.select()
        # else:
        #     interface(var.get() - 1)

        interface(0)
        black.select()
        
        p.protocol('WM_DELETE_WINDOW', rel1)
        p.mainloop()

    def criar_alarme():
        global active_edit;global active_delete;global cont_exibir_det;global obs;global ok
        global remove;global lista_alarmes;global alarmes;global cont;global add;global lbl1
        global rigid_lapis;global rigid_lixeira;global rigid_warning;global lapis;global lixeira
        global warning;global a;global scroll_alarmes;global bt_id;global apply;global cancel;global edit

        alarm_managment = Toplevel(window)
        alarm_managment.title('Gerenciador de alarmes')
        alarm_managment.geometry('400x350+540+210')
        alarm_managment['bg'] = palet_color[0]['BG']
        alarm_managment.resizable(0, 0)
        alarm_managment.grab_set()
        # alarm_managment.iconbitmap(resource_path('media/icons/icons/alarm.ico'))
        alarm_managment.iconbitmap('C:\\Users\\Paulo Thiago\\Downloads\\scripts\\python_curso_em_video\\Exercicios e Ideias\\Exercicios extras\\cronometro\\media\\icons\\icons\\alarm.ico')
        #hora = datetime.now().strftime('%H:%M')
        active_edit, active_delete, cont_exibir_det = True, True, 0

        def criar():
            global h;global m;global limit;global alarmes;global cont;global s1;global s2;global temp;global r_cont
            global hora;global c_titulo;global lbl_tit1;global t_hora;global temp;global t_txt;global obs
            global lbl_txt;global c_txt;global cont_exibir_det;global lbl_tit;global scroll_alarmes;global ok

            h = m = s1 = s2 = ''
            cont += 1
            add.config(state = DISABLED)
            lista_alarmes.config(state = DISABLED)
            remove.config(state = DISABLED)
            ok.config(state = DISABLED)
            obs.destroy()

            if cont_exibir_det != 0:
                c_titulo.destroy();lbl_tit1.destroy();lbl_tit.destroy()
                t_hora.destroy();temp.destroy();t_txt.destroy();
                lbl_txt.destroy();c_txt.destroy()

            def cancelar():
                global cont;global cancel;global apply
                global lista_alarmes;global obs;global ok

                tit.destroy();lbl_tit.destroy();hora.destroy()
                t_hora.destroy();minutos.destroy();t_min.destroy()
                t_txt.destroy();temp.destroy();txt.destroy()

                obs = Message(alarm_managment, text = 'OBS.: Os alarmes so seram ativados apos clicar no botao \'Ok\'', font = ('LCDMono2', 16), 
                            bg = palet_color[0]['BG'], fg = palet_color[0]['FG'], justify = LEFT, width = 230)
                obs.place(x = 165, y = 25)

                cancel.config(state = DISABLED)
                add.config(state = ACTIVE)
                apply.config(state = DISABLED)
                lista_alarmes.config(state = NORMAL)
                ok.config(state = ACTIVE)
                cont -= 1

            cancel.config(state = ACTIVE, command = cancelar)

            def salvar():
                global h;global m;global alarmes;global cont;global obs
                lista_alarmes.config(state = NORMAL)
                if hora.get() == '':
                    h = '00'
                elif len(hora.get()) == 1:
                    h = '0' + hora.get()
                else:
                    if int(hora.get()) > 23:
                        h = '23'
                    elif int(hora.get()) < 0:
                        h = '00'
                    else:
                        h = hora.get()
                if minutos.get() == '':
                    m = '00'
                elif len(minutos.get()) == 1:
                    m = '0' + minutos.get()
                else:
                    if int(minutos.get()) > 59:
                        m = '59'
                    elif int(minutos.get()) < 0:
                        m = '00'
                    else:
                        m = minutos.get()

                temp.config(text = h + ':' + m + ' h')
                alarmes.append({'titulo': tit.get(), 
                                'hora': h + ':' + m, 
                                'notas': txt.get('1.0', 'end')})
                lista_alarmes.insert(END, alarmes[cont - 1]['titulo'])
                add.config(state = ACTIVE)
                apply.config(state = DISABLED)
                cancel.config(state = DISABLED)
                scroll_alarmes.config(command = lista_alarmes.yview)
                ok.config(state = ACTIVE)

                obs = Message(alarm_managment, text = 'OBS.: Os alarmes so seram ativados apos clicar no botao \'Ok\'', font = ('LCDMono2', 16), 
                            bg = palet_color[0]['BG'], fg = palet_color[0]['FG'], justify = LEFT, width = 230)
                obs.place(x = 165, y = 25)
                
                tit.destroy();lbl_tit.destroy();hora.destroy()
                t_hora.destroy();minutos.destroy();t_min.destroy()
                t_txt.destroy();temp.destroy();txt.destroy();

            def hora():
                global h
                if 0 <= int(hora.get()) <= 9:
                    h = '0' + hora.get()
                    if m != '':
                        temp.config(text = h + ':' + m + ' h')
                    else:
                        temp.config(text = h + ':00' + ' h')
                else:
                    h = hora.get()
                    if m != '':
                        temp.config(text = h + ':' + m + ' h')
                    else:
                        temp.config(text = h + ':00' + ' h')

            def minu():
                global m
                if 0 <= int(minutos.get()) <= 9:
                    m = '0' + minutos.get()
                    if h != '':
                        temp.config(text = h + ':' + m + ' h')
                    else:
                        temp.config(text = '00:' + m + ' h')
                else:
                    m = minutos.get()
                    if h != '':
                        temp.config(text = h + ':' + m + ' h')
                    else:
                        temp.config(text = '00:' + m + ' h')

            def write1(*args):
                global s2;global temp;global s1;global hora

                if s2 == '':
                    s2 = '00'
                s1 = limit1.get()
                if len(s1) > 0:
                    if not s1[-1].isdigit():
                        limit1.set(s1[:-1])
                    else:
                        limit1.set(s1[:2])
                try:
                    s1 = list(s1)
                    if s1 != []:
                        if len(s1) > 1 and int(s1[0]) > 2:
                            s1.pop(0)
                            s1.insert(0, '2')
                        if int(s1[0]) >= 2:
                            if len(s1) >= 2 and int(s1[1]) > 3:
                                s1.pop(1)
                                s1.insert(1, '3')
                        if len(s1) == 1:
                            s1.insert(0, '0')
                    else:
                        s1 = ['0', '0']

                    s1 = str(s1[0] + s1[1])
                    temp.config(text = f'{s1[:2]}:{s2[:2]} h')
                except:
                    print()

            def write2(*args):
                global s2;global temp;global s1;global hora

                if s1 == '':
                    s1 = '00'
                s2 = limit2.get()
                if len(s2) > 0:
                    if not s2[-1].isdigit():
                        limit2.set(s2[:-1])
                    else:
                        limit2.set(s2[:2])
                try:
                    s2 = list(s2)
                    if s2 != []:
                        if len(s2) > 1 and int(s2[0]) > 5:
                            s2.pop(0)
                            s2.insert(0, '5')
                        if int(s2[0]) >= 5:
                            if len(s2) >= 2 and int(s2[1]) > 9:
                                s2.pop(1)
                                s2.insert(1, '9')
                        if len(s2) == 1:
                            s2.insert(0, '0')
                    else:
                        s2 = ['0', '0']

                    s2 = str(s2[0] + s2[1])
                    temp.config(text = f'{s1[:2]}:{s2[:2]} h')
                except:
                    print()

            def write_tit(*args):
                s = titulo.get()
                titulo.set(s[:18])
                if s == '':
                    apply.config(state = DISABLED)
                else:
                    apply.config(state = ACTIVE)

            limit1, limit2, titulo = StringVar(), StringVar(), StringVar()
            limit1.trace('w', write1)
            limit2.trace('w', write2)
            titulo.trace('w', write_tit)

            tit = Entry(alarm_managment, width = 25, bg = palet_color[0]['BG'], bd = 1, 
                        fg = palet_color[0]['FG'], font = ('LCDMono2'), 
                        selectbackground = palet_color[0]['FG'], 
                        selectforeground = palet_color[0]['BG'], 
                        insertbackground = palet_color[0]['FG'], 
                        insertwidth = 3, textvariable = titulo)
            tit.place(x = 180, y = 50)

            lbl_tit = Label(alarm_managment, text = 'Titulo', font = ('LCDMono2', 10), 
                            bg = palet_color[0]['BG'], fg = palet_color[0]['FG'])
            lbl_tit.place(x = 177, y = 30)

            hora = Spinbox(alarm_managment, from_ = 0, to = 23, width = 3, 
                        bg = palet_color[0]['BG'], fg = palet_color[0]['FG'], 
                        activebackground = palet_color[0]['BG'], textvariable = limit1, 
                        font = ('LCDMono2', 25), selectbackground = palet_color[0]['FG'], 
                        selectforeground = palet_color[0]['BG'], bd = 0, command = hora, 
                        buttonbackground = palet_color[0]['BG'])
            hora.place(x = 180, y = 105)

            t_hora = Label(alarm_managment, text = 'Hora', 
                        font = ('LCDMono2', 10), 
                        bg = palet_color[0]['BG'], fg = palet_color[0]['FG'])
            t_hora.place(x = 177, y = 85)

            minutos = Spinbox(alarm_managment, from_ = 0, to = 59, width = 3, 
                        bg = palet_color[0]['BG'], fg = palet_color[0]['FG'], 
                        activebackground = palet_color[0]['BG'], textvariable = limit2, 
                        font = ('LCDMono2', 25), selectbackground = palet_color[0]['FG'], 
                        selectforeground = palet_color[0]['BG'], bd = 0, command = minu, 
                        buttonbackground = palet_color[0]['BG'])
            minutos.place(x = 260, y = 105)

            t_min = Label(alarm_managment, text = 'Minutos', 
                        font = ('LCDMono2', 10), 
                        bg = palet_color[0]['BG'], fg = palet_color[0]['FG'])
            t_min.place(x = 257, y = 85)

            t_txt = Label(alarm_managment, text = 'Anotacao', 
                        font = ('LCDMono2', 10), 
                        bg = palet_color[0]['BG'], fg = palet_color[0]['FG'])
            t_txt.place(x = 177, y = 200)

            txt = Text(alarm_managment, width = 30, height = 8, font = ('LCDMono2', 10), 
                    fg = palet_color[0]['FG'], bg = palet_color[0]['BG'], insertbackground = palet_color[0]['FG'], 
                    selectforeground = palet_color[0]['BG'], insertwidth = 3, 
                    selectbackground = palet_color[0]['FG'])
            txt.place(x = 177, y = 220)

            temp = Label(alarm_managment, text = '00:00 h', 
                    fg = palet_color[0]['FG'], font = ('LCDMono2', 18), 
                    bg = palet_color[0]['BG'])
            temp.place(x = 177, y = 160)
            apply.config(command = salvar)

        def editar():
            global h;global m;global limit;global alarmes;global cont;global s1;global s2
            global temp;global hora;global idx;global active_edit;global c_titulo;global ok
            global lbl_tit1;global t_hora;global t_txt;global lbl_txt;global c_txt
            global cont_exibir_det;global lbl_tit;global scroll_alarmes;global obs
            
            active_edit = False
            cont += 1
            edit['state'] = DISABLED
            idx = lista_alarmes.curselection()[0]
            lista_alarmes.config(state = DISABLED)
            remove.config(state = DISABLED)
            ok.config(state = DISABLED)
            add.config(state = DISABLED)
            obs.destroy()

            if cont_exibir_det != 0:
                c_titulo.destroy();lbl_tit1.destroy();t_hora.destroy()
                temp.destroy();t_txt.destroy();lbl_txt.destroy()
                c_txt.destroy();lbl_tit.destroy()

            def cancelar():
                global cont;global cancel;global apply;global ok
                global lista_alarmes;global active_edit;global obs
                
                tit.destroy();lbl_tit.destroy();hora.destroy()
                t_hora.destroy();minutos.destroy();t_min.destroy()
                t_txt.destroy();temp.destroy();txt.destroy()

                obs = Message(alarm_managment, text = 'OBS.: Os alarmes so seram ativados apos clicar no botao \'Ok\'', font = ('LCDMono2', 16), 
                            bg = palet_color[0]['BG'], fg = palet_color[0]['FG'], justify = LEFT, width = 230)
                obs.place(x = 165, y = 25)

                cancel.config(state = DISABLED)
                apply.config(state = DISABLED)
                lista_alarmes.config(state = NORMAL)
                ok.config(state = ACTIVE)
                cont -= 1
                active_edit = True

            cancel.config(state = ACTIVE, command = cancelar)

            def salvar():
                global h;global m;global alarmes;global active_edit
                global lista_alarmes;global cont;global obs

                lista_alarmes.config(state = NORMAL)
                if hora.get() == '':
                    h = '00'
                elif len(hora.get()) == 1:
                    h = '0' + hora.get()
                else:
                    if int(hora.get()) > 23:
                        h = '23'
                    elif int(hora.get()) < 0:
                        h = '00'
                    else:
                        h = hora.get()
                if minutos.get() == '':
                    m = '00'
                elif len(minutos.get()) == 1:
                    m = '0' + minutos.get()
                else:
                    if int(minutos.get()) > 59:
                        m = '59'
                    elif int(minutos.get()) < 0:
                        m = '00'
                    else:
                        m = minutos.get()
                temp.config(text = h + ':' + m + ' h')
                alarmes[idx]['titulo'] = tit.get()
                alarmes[idx]['hora'] = h + ':' + m
                alarmes[idx]['notas'] = txt.get('1.0', 'end')
                lista_alarmes.delete(idx)
                lista_alarmes.insert(idx, alarmes[idx]['titulo'])
                add.config(state = ACTIVE)
                apply.config(state = DISABLED)
                cancel.config(state = DISABLED)
                ok.config(state = ACTIVE)
                add.config(state = ACTIVE)
                scroll_alarmes.config(command = lista_alarmes.yview)
                active_edit = True
                
                obs = Message(alarm_managment, text = 'OBS.: Os alarmes so seram ativados apos clicar no botao \'Ok\'', font = ('LCDMono2', 16), 
                            bg = palet_color[0]['BG'], fg = palet_color[0]['FG'], justify = LEFT, width = 230)
                obs.place(x = 165, y = 25)
                
                tit.destroy();lbl_tit.destroy();hora.destroy()
                t_hora.destroy();minutos.destroy();t_min.destroy()
                t_txt.destroy();temp.destroy();txt.destroy()

            def hora():
                global h
                if 0 <= int(hora.get()) <= 9:
                    h = '0' + hora.get()
                    if m != '':
                        temp.config(text = h + ':' + m + ' h')
                    else:
                        temp.config(text = h + ':00' + ' h')
                else:
                    h = hora.get()
                    if m != '':
                        temp.config(text = h + ':' + m + ' h')
                    else:
                        temp.config(text = h + ':00' + ' h')

            def minu():
                global m
                if 0 <= int(minutos.get()) <= 9:
                    m = '0' + minutos.get()
                    if h != '':
                        temp.config(text = h + ':' + m + ' h')
                    else:
                        temp.config(text = '00:' + m + ' h')
                else:
                    m = minutos.get()
                    if h != '':
                        temp.config(text = h + ':' + m + ' h')
                    else:
                        temp.config(text = '00:' + m + ' h')

            def write1(*args):
                global s2;global temp;global s1;global hora

                if s2 == '':
                    s2 = '00'
                s1 = limit1.get()
                if len(s1) > 0:
                    if not s1[-1].isdigit():
                        limit1.set(s1[:-1])
                    else:
                        limit1.set(s1[:2])
                try:
                    s1 = list(s1)
                    if s1 != []:
                        if len(s1) > 1 and int(s1[0]) > 2:
                            s1.pop(0)
                            s1.insert(0, '2')
                        if int(s1[0]) >= 2:
                            if len(s1) >= 2 and int(s1[1]) > 3:
                                s1.pop(1)
                                s1.insert(1, '3')
                        if len(s1) == 1:
                            s1.insert(0, '0')
                    else:
                        s1 = ['0', '0']

                    s1 = str(s1[0] + s1[1])
                    temp.config(text = f'{s1[:2]}:{s2[:2]} h')
                except:
                    print()

            def write2(*args):
                global s2;global temp;global s1;global hora

                if s1 == '':
                    s1 = '00'
                s2 = limit2.get()
                if len(s2) > 0:
                    if not s2[-1].isdigit():
                        limit2.set(s2[:-1])
                    else:
                        limit2.set(s2[:2])
                try:
                    s2 = list(s2)
                    if s2 != []:
                        if len(s2) > 1 and int(s2[0]) > 5:
                            s2.pop(0)
                            s2.insert(0, '5')
                        if int(s2[0]) >= 5:
                            if len(s2) >= 2 and int(s2[1]) > 9:
                                s2.pop(1)
                                s2.insert(1, '9')
                        if len(s2) == 1:
                            s2.insert(0, '0')
                    else:
                        s2 = ['0', '0']

                    s2 = str(s2[0] + s2[1])
                    temp.config(text = f'{s1[:2]}:{s2[:2]} h')
                except:
                    print()

            def write_tit(*args):
                s = titulo.get()
                titulo.set(s[:18])
                if s == '':
                    apply.config(state = DISABLED)
                else:
                    apply.config(state = ACTIVE)

            limit1, limit2, titulo = StringVar(), StringVar(), StringVar()
            limit1.trace('w', write1)
            limit2.trace('w', write2)
            titulo.trace('w', write_tit)

            tit = Entry(alarm_managment, width = 25, bg = palet_color[0]['BG'], bd = 1, 
                        fg = palet_color[0]['FG'], font = ('LCDMono2'), 
                        selectbackground = palet_color[0]['FG'], 
                        selectforeground = palet_color[0]['BG'], 
                        insertbackground = palet_color[0]['FG'], exportselection = 0, 
                        insertwidth = 3, textvariable = titulo)
            tit.insert(END, alarmes[lista_alarmes.curselection()[0]]['titulo'])
            tit.place(x = 180, y = 50)

            lbl_tit = Label(alarm_managment, text = 'Titulo', font = ('LCDMono2', 10), 
                            bg = palet_color[0]['BG'], fg = palet_color[0]['FG'])
            lbl_tit.place(x = 177, y = 30)

            hora = Spinbox(alarm_managment, from_ = 0, to = 23, width = 3, 
                        bg = palet_color[0]['BG'], fg = palet_color[0]['FG'], 
                        activebackground = palet_color[0]['BG'], textvariable = limit1, 
                        font = ('LCDMono2', 25), selectbackground = palet_color[0]['FG'], 
                        selectforeground = palet_color[0]['BG'], bd = 0, command = hora, 
                        buttonbackground = palet_color[0]['BG'])
            hora.delete(0, 'end')
            hora.insert(END, alarmes[lista_alarmes.curselection()[0]]['hora'][:2])
            hora.place(x = 180, y = 105)

            t_hora = Label(alarm_managment, text = 'Hora', 
                        font = ('LCDMono2', 10), 
                        bg = palet_color[0]['BG'], fg = palet_color[0]['FG'])
            t_hora.place(x = 177, y = 85)

            minutos = Spinbox(alarm_managment, from_ = 0, to = 59, width = 3, 
                        bg = palet_color[0]['BG'], fg = palet_color[0]['FG'], 
                        activebackground = palet_color[0]['BG'], textvariable = limit2, 
                        font = ('LCDMono2', 25), selectbackground = palet_color[0]['FG'], 
                        selectforeground = palet_color[0]['BG'], bd = 0, command = minu, 
                        buttonbackground = palet_color[0]['BG'])
            minutos.delete(0, 'end')
            minutos.insert(END, alarmes[lista_alarmes.curselection()[0]]['hora'][3:])
            minutos.place(x = 260, y = 105)

            t_min = Label(alarm_managment, text = 'Minutos', 
                        font = ('LCDMono2', 10), 
                        bg = palet_color[0]['BG'], fg = palet_color[0]['FG'])
            t_min.place(x = 257, y = 85)

            t_txt = Label(alarm_managment, text = 'Anotacao', 
                        font = ('LCDMono2', 10), 
                        bg = palet_color[0]['BG'], fg = palet_color[0]['FG'])
            t_txt.place(x = 177, y = 200)

            txt = Text(alarm_managment, width = 30, height = 8, font = ('LCDMono2', 10), 
                    fg = palet_color[0]['FG'], bg = palet_color[0]['BG'], insertbackground = palet_color[0]['FG'], 
                    selectforeground = palet_color[0]['BG'], insertwidth = 3, 
                    selectbackground = palet_color[0]['FG'])
            txt.insert(END, alarmes[lista_alarmes.curselection()[0]]['notas'])
            txt.place(x = 177, y = 220)

            temp = Label(alarm_managment, text = alarmes[lista_alarmes.curselection()[0]]['hora'] + ' h', 
                    fg = palet_color[0]['FG'], font = ('LCDMono2', 18), 
                    bg = palet_color[0]['BG'])
            temp.place(x = 177, y = 160)
            apply.config(command = salvar)

        lbl1 = Label(alarm_managment, text = 'Alarmes', 
                    bg = palet_color[0]['BG'], fg = palet_color[0]['FG'], 
                    font = ('LCDMono2', 18))
        lbl1.pack(anchor = NW, fill = 'none')

        # rigid_lapis = PhotoImage(file = resource_path('media/icons/lapis.png'))
        rigid_lapis = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Downloads\\scripts\\python_curso_em_video\\Exercicios e Ideias\\Exercicios extras\\cronometro\\media\\icons\\lapis.png')
        # rigid_lixeira = PhotoImage(file = resource_path('media/icons/lixeira.png'))
        rigid_lixeira = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Downloads\\scripts\\python_curso_em_video\\Exercicios e Ideias\\Exercicios extras\\cronometro\\media\\icons\\lixeira.png')
        # rigid_warning = PhotoImage(file = resource_path('media/icons/warning.png'))
        rigid_warning = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Downloads\\scripts\\python_curso_em_video\\Exercicios e Ideias\\Exercicios extras\\cronometro\\media\\icons\\warning.png')

        lapis = rigid_lapis.subsample(38, 38)
        lixeira = rigid_lixeira.subsample(38, 38)
        warning = rigid_warning.subsample(32, 32)

        a = Frame(alarm_managment)
        a.place(x = 0, y = 28)

        scroll_alarmes = Scrollbar(a, bg = palet_color[0]['BG'], activebackground = palet_color[0]['BG'], bd = 0, 
                                elementborderwidth = -5, highlightbackground = palet_color[0]['BG'], 
                                highlightcolor = palet_color[0]['BG'])
        scroll_alarmes.pack(side = RIGHT, fill = 'y')

        def alarmar():
            for al in alarmes:
                print(al['hora'])

        # test = Button(alarm_managment, text = 'Don\'t click!', command = alarmar)
        # test.pack()

        def delete():
            global cont;global active_delete
            active_delete = False

            confirmation = Toplevel(alarm_managment)
            confirmation.geometry('480x150+466+294')
            confirmation.resizable(0, 0)
            #confirmation.overrideredirect(1)
            confirmation.attributes("-toolwindow", 1)
            confirmation['bg'] = palet_color[0]['BG']

            remove.config(state = DISABLED)
            edit.config(state = DISABLED)
            add.config(state = DISABLED)
            
            def sim():
                global cont;global active_delete;global obs
                alarmes.pop(lista_alarmes.curselection()[0])
                lista_alarmes.delete(lista_alarmes.curselection()[0])
                cont -= 1
                active_delete = True
                add.config(state = ACTIVE)

                obs = Message(alarm_managment, text = 'OBS.: Os alarmes so seram ativados apos clicar no botao \'Ok\'', font = ('LCDMono2', 16), 
                            bg = palet_color[0]['BG'], fg = palet_color[0]['FG'], justify = LEFT, width = 230)
                obs.place(x = 165, y = 25)
                
                c_titulo.destroy();lbl_tit1.destroy();t_hora.destroy()
                temp.destroy();t_txt.destroy();lbl_txt.destroy()
                c_txt.destroy();lbl_tit.destroy();confirmation.destroy()

            def nao():
                global active_delete
                confirmation.destroy()
                active_delete = True
                add.config(state = ACTIVE)
                remove.config(state = ACTIVE)

            w1 = Frame(confirmation, bg = palet_color[0]['BG'])
            w1.pack(anchor = NW)
            w2 = Frame(confirmation, bg = palet_color[0]['BG'])
            w2.pack(anchor = SE, side = BOTTOM)

            lbl_warning = Label(w1, image = warning, 
                                bg = palet_color[0]['BG'])
            lbl_warning.pack(anchor = NW, side = LEFT, expand = False)

            lbl_warning1 = Label(w1, image = warning, 
                                bg = palet_color[0]['BG'])
            lbl_warning1.pack(side = LEFT, anchor = NW, expand = False)

            lbl_warning_txt = Label(w1, text = 'Apagar', 
                                    fg = palet_color[0]['FG'], bg = palet_color[0]['BG'], 
                                    font = ('LCDMono2', 20), pady = 8)
            lbl_warning_txt.pack(side = LEFT, anchor = NW, before = lbl_warning1, expand = False)

            lbl_warning_txt1 = Label(confirmation, text = f'Voce realmente deseja apagar o alarme "{lista_alarmes.get(lista_alarmes.curselection()[0])}"?', 
                                    font = ('LCDMono2', 12), fg = palet_color[0]['FG'], bg = palet_color[0]['BG'])
            lbl_warning_txt1.pack(anchor = NW, side = LEFT, expand = False)

            n = Button(w2, text = 'Nao', font = ('LCDMono2', 16), 
                    bg = palet_color[0]['BG'], fg = palet_color[0]['FG'], activebackground = palet_color[0]['BG'], 
                    activeforeground = palet_color[0]['AC_FG'], padx = 20, bd = 0, 
                    command = nao)
            n.pack(anchor = SE, side = RIGHT)

            s = Button(w2, text = 'Sim', font = ('LCDMono2', 16), bd = 0, 
                    bg = palet_color[0]['BG'], fg = palet_color[0]['FG'], activebackground = palet_color[0]['BG'], 
                    activeforeground = palet_color[0]['AC_FG'], padx = 20, command = sim)
            s.pack(anchor = SE, side = BOTTOM)

            winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS+winsound.SND_NODEFAULT+winsound.SND_ASYNC)

            confirmation.mainloop()


        def CurSelet(evt):
            global idx;global c_titulo;global lbl_tit1
            global lbl_tit;global t_hora;global temp;global t_txt
            global lbl_txt;global c_txt;global cont_exibir_det;global obs

            idx = lista_alarmes.curselection()[0]
            if active_delete == True:
                remove.config(state = ACTIVE)
                if active_edit == True:
                    edit.config(state = ACTIVE)
                add.config(state = ACTIVE)
            if len(alarmes) >= 1:
                global c_titulo;global lbl_tit1;global lbl_tit
                global t_hora;global temp;global t_txt;global lbl_txt
                global c_txt;global cont_exibir_det;global obs

                obs.destroy()
                cont_exibir_det += 1

                try:
                    c_titulo.destroy();lbl_tit1.destroy();lbl_tit.destroy()
                    t_hora.destroy();temp.destroy();t_txt.destroy()
                    lbl_txt.destroy();c_txt.destroy()
                except:
                    print('As variáveis de exibição ainda não foram definidas!')

                h1 = alarmes[lista_alarmes.curselection()[0]]['hora']
                t1 = alarmes[lista_alarmes.curselection()[0]]['titulo']
                txt1 = alarmes[lista_alarmes.curselection()[0]]['notas']

                c_titulo = Canvas(alarm_managment, bg = palet_color[0]['BG'], height = 20, 
                                width = 200, highlightthickness = 0)
                c_titulo.place(x = 177, y = 50)

                lbl_tit1 = Label(alarm_managment, text = t1, font = ('LCDMono2', 10), 
                                bg = palet_color[0]['BG'], fg = palet_color[0]['FG'])
                lbl_tit1.place(x = 178, y = 50)

                lbl_tit = Label(alarm_managment, text = 'Titulo', font = ('LCDMono2', 10), 
                                bg = palet_color[0]['BG'], fg = palet_color[0]['FG'])
                lbl_tit.place(x = 177, y = 30)

                t_hora = Label(alarm_managment, text = 'Alarme definido as:', 
                            font = ('LCDMono2', 10), 
                            bg = palet_color[0]['BG'], fg = palet_color[0]['FG'])
                t_hora.place(x = 177, y = 85)

                temp = Label(alarm_managment, text = f'{h1} h', 
                            fg = palet_color[0]['FG'], font = ('LCDMono2', 25), 
                            bg = palet_color[0]['BG'])
                temp.place(x = 177, y = 105)

                t_txt = Label(alarm_managment, text = 'Anotacao', 
                            font = ('LCDMono2', 10), 
                            bg = palet_color[0]['BG'], fg = palet_color[0]['FG'])
                t_txt.place(x = 177, y = 160)

                c_txt = Canvas(alarm_managment, bg = palet_color[0]['BG'], height = 130, 
                            width = 200, highlightthickness = 0)
                c_txt.place(x = 177, y = 180)

                lbl_txt = Message(alarm_managment, text = txt1[:240], font = ('LCDMono2', 10), 
                                bg = palet_color[0]['BG'], fg = palet_color[0]['FG'], justify = LEFT, 
                                width = 188)
                lbl_txt.place(x = 177, y = 181)

        def okay():
            global cr_active
            def_alarm = Toplevel(alarm_managment)
            def_alarm['bg'] = palet_color[0]['BG']
            def_alarm.geometry('380x160+515+280')
            def_alarm.resizable(0, 0)
            def_alarm.attributes('-toolwindow', 1)

            def rel():
                if cr_active == False:
                    relogio()
                else:
                    cron()
            
            def sair():
                rel()
                def_alarm.destroy()
                alarm_managment.destroy()

            if lista_alarmes.get(END) != '':
                ok_msg = 'Os alarmes foram definidos\n\ncom sucesso!'
            else:
                ok_msg = 'Nenhum alarme foi definido!'
            
            # i = PhotoImage(file = resource_path('media/icons/info.png'))
            i = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Downloads\\scripts\\python_curso_em_video\\Exercicios e Ideias\\Exercicios extras\\cronometro\\media\\icons\\info.png')
            info = i.subsample(16, 16)

            lbl_info = Label(def_alarm, image = info, bg = palet_color[0]['BG'], 
                             height = 120, width = 120)
            lbl_info.pack(anchor = NW, side = LEFT)
            lbl_info_txt = Message(def_alarm, text = ok_msg, 
                                   bg = palet_color[0]['BG'], fg = palet_color[0]['FG'], font = ('LCDMono2', 12), 
                                   pady = 44, width = 220)
            lbl_info_txt.pack(anchor = NW)

            ok = Button(def_alarm, text = 'Ok', font = ('LCDMono2', 18), bd = 0, 
                        activebackground = palet_color[0]['BG'], activeforeground = palet_color[0]['AC_FG'], 
                        bg = palet_color[0]['BG'], fg = palet_color[0]['FG'], padx = 30, command = sair)
            ok.pack(anchor = SE, side = BOTTOM)
            
            if lista_alarmes.get(END) != '':
                winsound.PlaySound('SystemAsterisk', winsound.SND_ALIAS+winsound.SND_NODEFAULT+winsound.SND_ASYNC)
            else:
                winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS+winsound.SND_NODEFAULT+winsound.SND_ASYNC)

            def_alarm.protocol('WM_DELETE_WINDOW', rel)
            def_alarm.mainloop()


        lista_alarmes = Listbox(a, width = 18, height = 16, font = ('LCDMono2', 11), 
                                bg = palet_color[0]['BG'], fg = palet_color[0]['FG'], highlightcolor = palet_color[0]['FG'], 
                                selectbackground = palet_color[0]['FG'], selectforeground = palet_color[0]['BG'], 
                                selectmode = SINGLE, highlightthickness = 0, 
                                yscrollcommand = scroll_alarmes.set)
        lista_alarmes.bind('<<ListboxSelect>>', CurSelet)
        lista_alarmes.pack(anchor = NW)

        bt_id = Frame(alarm_managment, bg = palet_color[0]['BG'])
        bt_id.pack(anchor = SE, side = BOTTOM)

        apply = Button(bt_id, text = 'Aplicar', font = ('LCDMono2', 13), 
                    fg = palet_color[0]['FG'], bg = palet_color[0]['BG'], bd = 0, 
                    activebackground = palet_color[0]['BG'], state = DISABLED, 
                    activeforeground = palet_color[0]['AC_FG'], padx = 5)
        apply.pack(anchor = SE, side = RIGHT)

        cancel = Button(bt_id, text = 'Cancelar', font = ('LCDMono2', 13), 
                    fg = palet_color[0]['FG'], bg = palet_color[0]['BG'], bd = 0, 
                    activebackground = palet_color[0]['BG'], state = DISABLED, 
                    activeforeground = palet_color[0]['AC_FG'], padx = 5)
        cancel.pack(anchor = SE, side = RIGHT)

        ok = Button(bt_id, text = 'Ok', font = ('LCDMono2', 13), 
                    fg = palet_color[0]['FG'], bg = palet_color[0]['BG'], bd = 0, 
                    activebackground = palet_color[0]['BG'], state = DISABLED, 
                    activeforeground = palet_color[0]['AC_FG'], padx = 5, 
                    command = okay)
        ok.pack(anchor = SE, side = BOTTOM)

        edit = Button(alarm_managment, image = lapis, bg = palet_color[0]['BG'], bd = 0, 
                    activebackground = palet_color[0]['BG'], state = DISABLED, 
                    height = 50, width = 50, command = editar)
        edit.pack(anchor = SW, side = BOTTOM)

        remove = Button(alarm_managment, image = lixeira, bg = palet_color[0]['BG'], bd = 0, 
                        activebackground = palet_color[0]['BG'], state = DISABLED, 
                        height = 50, width = 50, command = delete)
        remove.pack(anchor = SW, side = LEFT, before = edit)

        add = Button(alarm_managment, text = '+', bg = palet_color[0]['BG'], bd = 0, 
                    fg = palet_color[0]['FG'], font = ('Monospace', 20), 
                    activebackground = palet_color[0]['BG'], width = 3, 
                    activeforeground = palet_color[0]['AC_FG'], command = criar)
        add.pack(anchor = SW, side = LEFT, before = remove)

        if len(alarmes) == 0:
            obs = Message(alarm_managment, text = 'OBS.: Os alarmes so seram ativados apos clicar no botao \'Ok\'', font = ('LCDMono2', 16), 
                        bg = palet_color[0]['BG'], fg = palet_color[0]['FG'], justify = LEFT, width = 230)
            obs.place(x = 165, y = 25)

        alarm_managment.mainloop()

        
    def cron():
        global cronometro;global b_start;global b_stop;global b_reset;global text
        global h;global r_cont;global mode;global cr_active;global cr_cont;global add_alarm
        cr_cont += 1
        try:
            h.destroy()
        except:
            print('A variável \'h\' ainda não foi definida!')
        
        if cr_cont > 1:
            text.destroy()
            b_start.destroy()
            b_stop.destroy()
            b_reset.destroy()

        # window.iconbitmap(resource_path('media/icons/icons/main_window.ico'))
        window.iconbitmap('C:\\Users\\Paulo Thiago\\Downloads\\scripts\\python_curso_em_video\\Exercicios e Ideias\\Exercicios extras\\cronometro\\media\\icons\\icons\\main_window.ico')
        window.update_idletasks()
        cr_active = True
        cronometro = [0, 0, ':', 0, 0, ':', 0, 0, ':', 0, 0]
        reset = cronometro.copy()
        conf_reset = False
        quant_reset = 0

        def iniciar():
            global b_start;global b_stop;global b_reset
            global cronometro;global active;global text
            global mode;global add_alarm
            
            winsound.Beep(2000, 100)
            active = True
            
            add(text, s, cronometro)

            for c in range(0, 2):
                mode.entryconfig(c, state = DISABLED)
            
            add_alarm.entryconfig(1, state = DISABLED)

            def parar():
                global active
                winsound.Beep(1000, 100)
                active = False
                for c in range(0, 2):
                    mode.entryconfig(c, state = ACTIVE)
                
                add_alarm.entryconfig(1, state = ACTIVE)
                return active

            def resetar():
                global cronometro;global text

                winsound.Beep(800, 100)
                cronometro = [0, 0, ':', 0, 0, ':', 0, 0, ':', 0, 0]
                text['text'] = cronometro
                b_reset['state'] = DISABLED
                b_start['text'] = 'Iniciar'
                return cronometro

            b_stop['command'] = parar
            b_reset['command'] = resetar
            
            while active == True:
                add(text, s, cronometro)
                sleep(0.00719)
                if active == True:
                    b_start['state'] = DISABLED
                    b_reset['state'] = DISABLED
                    b_stop['state'] = ACTIVE
                window.update()

            if active == False:
                b_stop['state'] = DISABLED
                b_start['state'] = ACTIVE
                b_reset['state'] = ACTIVE
            if active == True:
                b_stop['state'] = ACTIVE
                b_start['state'] = DISABLED
                b_reset['state'] = DISABLED

            if cronometro == [0, 0, ':', 0, 0, ':', 0, 0, ':', 0, 0]:
                b_start['text'] = 'Iniciar'
            if cronometro != [0, 0, ':', 0, 0, ':', 0, 0, ':', 0, 0]:
                b_start['text'] = 'Retomar'


        text = Label(window, text = cronometro, 
                    font = ('LCDMono2', e, 'bold'), 
                    bg = palet_color[0]['BG'], 
                    fg = palet_color[0]['FG'])
        text.pack(expand = True, anchor = CENTER)

        b_start = Button(window, text = 'Iniciar', 
                        font = ('LCDMono2', 20), bd = 0, 
                        bg = palet_color[0]['BG'], fg = palet_color[0]['FG'], 
                        activebackground = palet_color[0]['BG'], 
                        activeforeground = palet_color[0]['AC_FG'], 
                        width = 7, command = iniciar)
        b_start.pack(expand = True, side = LEFT)

        b_stop = Button(window, text = 'Parar', 
                        font = ('LCDMono2', 20), 
                        bd = 0, bg = palet_color[0]['BG'], 
                        fg = palet_color[0]['FG'], width = 7, 
                        activebackground = palet_color[0]['BG'], 
                        activeforeground = palet_color[0]['AC_FG'], 
                        state = DISABLED)
        b_stop.pack(expand = True, side = LEFT)

        b_reset = Button(window, text = 'Resetar', 
                        font = ('LCDMono2', 20), 
                        bd = 0, bg = palet_color[0]['BG'], 
                        fg = palet_color[0]['FG'], width = 7, 
                        activebackground = palet_color[0]['BG'], 
                        activeforeground = palet_color[0]['AC_FG'], 
                        state = DISABLED)
        b_reset.pack(expand = True, side = RIGHT)

    var_scale = DoubleVar()
    n_show = 2

    def configs():
        global n_show;global scale
        n_show += 1
        
        def escala(var_scale):
            global e
            e = int(var_scale)
            text['font'] = ('LCDMono2', e)
            try:
                h['font'] = ('LCDMono2', (e + 40), 'bold')
            except:
                print('')

        if n_show % 2 == 0:
            show_conf['text'] = '/\\'
            scale.destroy()
        else:
            show_conf['text'] = '\\/'
            scale = Scale(window, variable = var_scale, bd = 0, 
                    bg = palet_color[0]['BG'], fg = palet_color[0]['FG'], font = ('LCDMono2', 10), 
                    activebackground = palet_color[0]['FG'], highlightbackground = palet_color[0]['BG'], 
                    highlightcolor = palet_color[0]['FG'], orient = HORIZONTAL, 
                    length = 200, from_ = 10, to_ = 90, sliderlength = 30, 
                    troughcolor = palet_color[0]['BG'], command = escala)
            scale.pack(anchor = S, side = BOTTOM, before = escala_txt)

    escala_txt = Label(window, text = 'Tamanho', font = ('LCDMono2', 10), 
                       bg = palet_color[0]['BG'], fg = palet_color[0]['FG'])
    escala_txt.pack(anchor = S, side = BOTTOM)

    show_conf = Button(window, text = '/\\', 
                       font = ('LCDMono2', 15), 
                       bg = palet_color[0]['BG'], fg = palet_color[0]['FG'], 
                       activebackground = palet_color[0]['BG'], 
                       activeforeground = palet_color[0]['AC_FG'], 
                       bd = 0, command = configs)
    show_conf.pack(anchor = S, side = BOTTOM, fill = 'both')

    cron()
    menubar = Menu(window, font = ('LCDMono2', 10))
    mode = Menu(menubar, tearoff = 0, font = ('LCDMono2', 10), 
                    bg = palet_color[0]['BG'], fg = palet_color[0]['FG'], bd = 0, 
                    activebackground = palet_color[0]['BG'], activeforeground = palet_color[0]['AC_FG'])

    add_alarm = Menu(menubar, tearoff = 0, font = ('LCDMono2', 10), 
                    bg = palet_color[0]['BG'], fg = palet_color[0]['FG'], bd = 0, 
                    activebackground = palet_color[0]['BG'], activeforeground = palet_color[0]['AC_FG'])

    editar = Menu(menubar, tearoff = 0, font = ('LCDMono2', 10), 
                    bg = palet_color[0]['BG'], fg = palet_color[0]['FG'], bd = 0, 
                    activebackground = palet_color[0]['BG'], activeforeground = palet_color[0]['AC_FG'])

    menubar.add_cascade(label = 'Modo', menu = mode)
    menubar.add_cascade(label = 'Alarme', menu = add_alarm)
    menubar.add_cascade(label = 'Personalizar', menu = editar)
    add_alarm.add_command(label = 'Gerenciar Alarmes', command = criar_alarme)
    editar.add_command(label = 'Preferencias', command = prefs)

    mode.add_radiobutton(label = 'Cronometro', command = cron)
    mode.add_radiobutton(label = 'Relogio', command = relogio)
    mode.add_radiobutton(label = 'Contagem Regressiva')
    mode.entryconfig(2, state = DISABLED)
    mode.add_separator()
    mode.add_command(label = 'Sair', command = window.destroy)
    window.config(menu = menubar)

import flet as ft
import random

# ==================== 数据层（完整题库） ====================
class Question:
    def __init__(self, qid, source, topic, question, answer, solution, options=None):
        self.id = qid
        self.source = source
        self.topic = topic
        self.question = question
        self.options = options
        self.answer = answer
        self.solution = solution
        self.is_done = False

def build_question_bank():
    """从文档中提取的所有题目（共32题）"""
    questions = []

    # -------------------- P7 --------------------
    questions.append(Question(
        "P7-1", "P7", "事件表示",
        "三次射击中，至少有一次没有击中靶子（等价于'三次射击不全击中靶子'）。\n请用事件A_i表示第i次击中，写出该事件的集合表达式。",
        "A₁' ∪ A₂' ∪ A₃' 或 (A₁A₂A₃)'",
        "至少一次未击中 = 不全击中 = 补集（三次全击中）"
    ))
    questions.append(Question(
        "P7-2", "P7", "事件表示",
        "前两次射击都没有击中靶子（即第一次未击中，且第二次也未击中）。",
        "A₁' ∩ A₂'",
        "两次都未击中，用交集表示。"
    ))
    questions.append(Question(
        "P7-3", "P7", "事件表示",
        "三次射击中，第二次击中，且恰好击中两次（即'第二次击中，第一次和第三次中只有一次击中'）。",
        "A₂ ∩ (A₁' A₃ ∪ A₁ A₃')",
        "第二次击中，且第一次和第三次恰好一次击中。"
    ))

    # -------------------- P10 --------------------
    questions.append(Question(
        "P10-1", "P10", "加法公式",
        "已知 A 与 B 互不相容，P(A∪B)=0.3，P(A)=0.1，求 P(B)。",
        "P(B)=0.2",
        "因为互不相容，P(AB)=0，由加法公式得 P(B)=0.3-0.1=0.2。"
    ))
    questions.append(Question(
        "P10-2", "P10", "古典概型",
        "袋中装有 5 个白球，3 个黑球，从中一次任取 2 个。\n(1) 求取到的 2 个球颜色不同的概率；\n(2) 求取到的 2 个球中有黑球的概率。",
        "(1) 15/28  (2) 9/14",
        "总事件 C(8,2)=28。\n(1) 颜色不同：C(5,1)C(3,1)=15 → 15/28\n(2) 有黑球：C(3,1)C(5,1)+C(3,2)=18 → 18/28=9/14"
    ))
    questions.append(Question(
        "P10-4", "P10", "古典概型",
        "袋中有红、黄、黑色球各一个，有放回地抽取三次，求下列事件的概率：\nA={三次都是红球}，B={三次未抽到黑球}，C={颜色全不相同}，D={颜色不全相同}。",
        "P(A)=1/27, P(B)=8/27, P(C)=6/27=2/9, P(D)=1-3/27=24/27=8/9",
        "总样本数 3³=27。\nA：1/27；B：每次只能取红或黄，2³=8，P=8/27；C：全排列 3! =6，P=6/27=2/9；D：不全相同=1-全相同(3种)=1-3/27=24/27=8/9"
    ))

    # -------------------- P21 --------------------
    questions.append(Question(
        "P21-1", "P21", "条件概率",
        "一批产品100件，正品80件，次品20件。甲厂生产60件（正品50件，次品10件），乙厂40件。记A={正品}，B={甲厂产品}，求 P(A), P(B), P(AB), P(B|A), P(A|B)。",
        "P(A)=0.8, P(B)=0.6, P(AB)=0.5, P(B|A)=5/8, P(A|B)=5/6",
        "P(A)=80/100=0.8；P(B)=60/100=0.6；P(AB)=50/100=0.5；P(B|A)=0.5/0.8=5/8；P(A|B)=0.5/0.6=5/6"
    ))
    questions.append(Question(
        "P21-2", "P21", "条件概率",
        "一批产品一、二、三等品各占60%，30%，10%。从中任取1件，结果不是三等品，求取到的是一等品的概率。",
        "2/3",
        "设A1=一等品，A2=二等品，A3=三等品。所求 P(A1|A1∪A2)=0.6/(0.6+0.3)=2/3"
    ))
    questions.append(Question(
        "P21-3", "P21", "条件概率",
        "10件产品中有4件不合格品，从中任取2件。已知所取2件中有1件不合格品，求另一件也是不合格品的概率。",
        "1/5",
        "设B={两件全不合格}，C={至少一件不合格}。P(B)=C(4,2)/C(10,2)=6/45=2/15；P(C)=1-C(6,2)/C(10,2)=1-15/45=2/3；所求=P(B)/P(C)= (2/15)/(2/3)=1/5"
    ))
    questions.append(Question(
        "P21-4", "P21", "条件概率",
        "已知 P(A)=1/4，P(B|A)=1/3，P(A|B)=1/2，求 P(A∪B)。",
        "1/3",
        "P(AB)=P(A)P(B|A)= (1/4)(1/3)=1/12；P(B)=P(AB)/P(A|B)= (1/12)/(1/2)=1/6；P(A∪B)=1/4+1/6-1/12=1/3"
    ))

    # -------------------- P25 --------------------
    questions.append(Question(
        "P25-1", "P25", "独立性",
        "设 P(AB)=0，则（  ）\nA. A和B不相容  B. A和B独立  C. P(A)=0或P(B)=0  D. P(A-B)=P(A)",
        "D",
        "P(AB)=0 ⇒ P(A-B)=P(A)-P(AB)=P(A)，故D正确。其余选项均不一定成立。",
        ["A. A和B不相容", "B. A和B独立", "C. P(A)=0或P(B)=0", "D. P(A-B)=P(A)"]
    ))
    questions.append(Question(
        "P25-2", "P25", "二项分布",
        "每次实验成功的概率为 p (0<p<1)，进行重复实验，求直到第10次实验才取得4次成功的概率。",
        "C(9,3) p^4 (1-p)^6",
        "前9次中恰有3次成功，且第10次成功。概率 = C(9,3) p^3 (1-p)^6 · p = C(9,3) p^4 (1-p)^6"
    ))

    # -------------------- 总习一 --------------------
    questions.append(Question(
        "Z1-1", "总习一", "事件表示",
        "有放回抽取三次，Ai表示第i次抽到废品。用事件集合表示：\n(1) 第一次和第二次至少抽到一件废品；\n(2) 只有第一次抽到废品；\n(3) 三次都抽到废品；\n(4) 至少有一次抽到废品；\n(5) 只有两次抽到废品。",
        "(1) A₁∪A₂  (2) A₁∩A₂'∩A₃'  (3) A₁A₂A₃  (4) A₁∪A₂∪A₃  (5) (A₁A₂A₃')∪(A₁A₂'A₃)∪(A₁'A₂A₃)",
        "按事件运算定义给出。"
    ))
    # 文档中还有Z1-4、Z1-5等，但描述不全，我们根据已知补充
    questions.append(Question(
        "Z1-5", "总习一", "概率加法",
        "设 A,B,C 是三个事件，且 P(A)=P(B)=P(C)=1/4，P(AB)=P(BC)=0，P(AC)=1/8，求 A,B,C 至少有一个发生的概率。",
        "5/8",
        "P(A∪B∪C)=P(A)+P(B)+P(C)-P(AB)-P(AC)-P(BC)+P(ABC)\n=3/4 - 1/8 + 0 = 5/8（因为P(AB)=P(BC)=0，所以P(ABC)=0）"
    ))
    questions.append(Question(
        "Z1-8", "总习一", "超几何/二项/不放回",
        "一批产品100件，其中98件正品，2件次品，从中任意抽取3件。\n分三种情况：一次拿3件；每次拿1件，取后放回，拿3次；每次拿1件，取后不放回，拿3次。\n求：(1) 取出的3件中恰有1件次品的概率；(2) 取出的3件中至少有1件次品的概率。",
        "一次拿3件：(1) C(2,1)C(98,2)/C(100,3) ≈0.0588 (2) 1-C(98,3)/C(100,3) ≈0.0594\n放回：(1) C(3,1)(0.02)(0.98)^2 ≈0.0576 (2) 1-(0.98)^3 ≈0.0588\n不放回(逐次)：(1) 同一次拿3件 (2) 同一次拿3件",
        "按超几何分布和二项分布计算。不放回与一次拿3件等价。"
    ))

    # -------------------- P37 --------------------
    questions.append(Question(
        "P37-2", "P37", "分布律",
        "随机变量 X 的分布律为 P{X=k}=k/15, k=1,2,3,4,5。\n求 (1) P(1/2<X<5/2)  (2) P(1≤X≤3)  (3) P(X>3)",
        "(1) 1/5  (2) 2/5  (3) 3/5",
        "(1) P(X=1)+P(X=2)=1/15+2/15=3/15=1/5\n(2) 1/15+2/15+3/15=6/15=2/5\n(3) 4/15+5/15=9/15=3/5"
    ))

    # -------------------- P40 --------------------
    questions.append(Question(
        "P40-3", "P40", "分布函数",
        "离散型随机变量 X：P{X=1}=0.3, P{X=3}=0.5, P{X=0.5}=0.2。\n(1) 写出分布函数 F(x)  (2) 求 P(0<X<4)",
        "(1) 分段函数见解析  (2) 1",
        "(1) F(x)=0 (x<0.5), 0.2 (0.5≤x<1), 0.5 (1≤x<3), 1 (x≥3)\n(2) P(0<X<4)=0.2+0.3+0.5=1"
    ))

    # -------------------- P53 --------------------
    questions.append(Question(
        "P53-1", "P53", "随机变量分布",
        "X 的分布：P{X=-2}=2a, P{X=-1}=1/10, P{X=0}=3a, P{X=1}=a, P{X=2}=a, P{X=3}=2a\n(1) 求 a  (2) 求 Y=X²-1 的分布",
        "(1) a=0.1  (2) P{Y=-1}=0.3, P{Y=0}=0.2, P{Y=3}=0.3, P{Y=8}=0.2",
        "(1) 9a+0.1=1 ⇒ a=0.1\n(2) Y 取值：-1,0,3,8；对应概率合并后如上。"
    ))

    # -------------------- 总习二 --------------------
    questions.append(Question(
        "Z2-2", "总习二", "二项分布",
        "若每次射击中靶的概率为0.7，求射击10炮：\n(1) 命中3炮的概率；\n(2) 至少命中3炮的概率；\n(3) 最可能命中几炮。",
        "(1) C(10,3)0.7^3 0.3^7 ≈0.0090\n(2) 1 - Σ_{k=0}^{2} C(10,k)0.7^k0.3^{10-k} ≈0.9984\n(3) 最可能命中7炮（因为 (n+1)p=7.7，取整为7）",
        "按二项分布计算。最可能命中次数为 [(n+1)p] 或 [(n+1)p]-1，此处 (10+1)*0.7=7.7，取整为7。"
    ))
    questions.append(Question(
        "Z2-6", "总习二", "分布律与分布函数",
        "设X为离散型随机变量，其分布律为 P{X=k}=q(1-q)^{k-1}, k=1,2,... (0<q<1)。\n(1) 求 q 值； (2) 求 X 的分布函数。",
        "(1) q 已经满足概率和=1，无需另求（几何分布）\n(2) F(x)=1-(1-q)^k, 当 k≤x<k+1 (k=1,2,...)",
        "这是几何分布，概率和为1。分布函数为 F(x)=P(X≤x)=1-(1-q)^{⌊x⌋}（x≥1）"
    ))

    # -------------------- P76 --------------------
    questions.append(Question(
        "P76-1", "P76", "二维随机变量",
        "设随机变量(X,Y)的概率密度为 f(x,y)= { 2, 0<x<y<1; 0, 其他 }。\n(1) X 和 Y 是否相互独立？\n(2) 求 Z=X+Y 的概率密度。",
        "(1) 不独立（因为联合密度不能分解为边缘密度乘积）\n(2) f_Z(z)= { 2z, 0<z<1; 2(2-z), 1≤z<2; 0, 其他 }",
        "(1) 边缘密度 f_X(x)=2(1-x) (0<x<1), f_Y(y)=2y (0<y<1)，乘积不等于联合密度，故不独立。\n(2) 用卷积公式，分段积分可得三角形分布。"
    ))
    questions.append(Question(
        "P76-3", "P76", "顺序统计量",
        "设随机变量X，Y相互独立，且服从同一分布。试证明：P{a<min{X,Y}≤b} = [P{X>a}]² - [P{X>b}]²。",
        "证明：P{min>a} = P(X>a,Y>a)=P(X>a)^2, 同理 min>b。则 P(a<min≤b)=P(min>a)-P(min>b)=[P(X>a)]²-[P(X>b)]²。",
        "利用独立性和min事件转化。"
    ))

    # -------------------- P85 --------------------
    questions.append(Question(
        "P85-5", "P85", "数学期望",
        "X 的分布律：P{X=-2}=0.1, -1:0.2, 0:0.3, 1:0.3, 2:0.1\n求 E(X), E(X²), E(3X²+5)",
        "E(X)=0.1, E(X²)=1.3, E(3X²+5)=8.9",
        "E(X)=(-2)(0.1)+(-1)(0.2)+0(0.3)+1(0.3)+2(0.1)=0.1\nE(X²)=4(0.1)+1(0.2)+0+1(0.3)+4(0.1)=1.3\nE(3X²+5)=3(1.3)+5=8.9"
    ))
    questions.append(Question(
        "P85-6", "P85", "连续型概率密度",
        "设连续型随机变量X的概率密度为 f(x)= { kx^a, 0<x<1; 0, 其他 }，其中 k>0, a>0。\n又已知 E(X)=0.75，求 k, a 的值。",
        "a=1, k=2",
        "由归一化 ∫₀¹ k x^a dx = k/(a+1)=1 ⇒ k=a+1。\nE(X)=∫₀¹ x·kx^a dx = k/(a+2) = 0.75。\n代入 k=a+1，得 (a+1)/(a+2)=0.75 ⇒ 4a+4=3a+6 ⇒ a=2, 则 k=3。\n（检查：E=3/4=0.75，正确）"
    ))
    questions.append(Question(
        "P85-9", "P85", "二维期望",
        "设(X,Y)的分布律为（略，可参考文档）\n(1) 求E(X), E(Y)；(2) 设Z=Y/X，求E(Z)；(3) 设Z=(X-Y)²，求E(Z)。",
        "（具体数值需查表，此处给出方法）",
        "按离散期望公式：E(X)=Σ x_i P(X=x_i)，E(Y)=Σ y_j P(Y=y_j)，E(Z)=Σ g(x,y) P(X=x,Y=y)。"
    ))

    # -------------------- P90 --------------------
    questions.append(Question(
        "P90-7", "P90", "二项分布",
        "X~b(n,p) 且 E(X)=3, D(X)=2。求 n, p 及 X 全部可能取值，并计算 P{X≤8}。",
        "n=9, p=1/3, X=0..9, P{X≤8}=1-(1/3)^9",
        "np=3, np(1-p)=2 ⇒ p=1/3, n=9\nX 可取 0~9\nP{X≤8}=1-P{X=9}=1-(1/3)^9"
    ))

    # -------------------- P98 --------------------
    questions.append(Question(
        "P98-6", "P98", "不相关与独立",
        "联合分布律（见文档），验证 X 和 Y 不相关且不独立。",
        "E(XY)=E(X)E(Y)=0，但 P(X=0,Y=0)≠P(X=0)P(Y=0)",
        "计算边缘分布得 E(X)=E(Y)=0，E(XY)=0，故不相关。\n但 P(X=0,Y=0)=0 ≠ (1/4)(1/4)=1/16，故不独立。"
    ))

    # -------------------- P107 --------------------
    questions.append(Question(
        "P107-12", "P107", "方差计算",
        "X1~U[0,6], X2~Exp(1/2), X3~P(3)，独立。Y=X1-2X2+3X3，求 D(Y)。",
        "46",
        "D(X1)=(6-0)²/12=3, D(X2)=1/(1/2)²=4, D(X3)=3\nD(Y)=3+4×4+9×3=3+16+27=46"
    ))
    questions.append(Question(
        "P107-17", "P107", "期望方差综合",
        "E(X)=2, E(Y)=4, D(X)=4, D(Y)=9, ρ=0.5。\n(1) U=3X²-2XY+Y²-3 的期望  (2) V=3X-Y+5 的方差",
        "(1) E(U)=24  (2) D(V)=27",
        "(1) E(X²)=8, E(Y²)=25, Cov=3, E(XY)=11 → E(U)=3*8-2*11+25-3=24\n(2) D(V)=9*4+9-2*3*Cov(X,Y)=36+9-18=27"
    ))

    # -------------------- P119 --------------------
    questions.append(Question(
        "P119-4", "P119", "样本统计",
        "某地区抽样调查200个居民户的月人均收入，得到统计资料（略）。求样本容量n, 样本均值X̄, 样本方差S²。",
        "n=200, X̄ = (Σ组中值×频数)/200, S² = [Σ组中值²×频数 - (Σ组中值×频数)²/200] / (200-1)",
        "按分组数据计算样本均值和方差。"
    ))

    # -------------------- P127, P132 有图片题目，文字描述不足，我们补充为概念题 --------------------
    questions.append(Question(
        "P127-1", "P127", "统计概念",
        "（根据图片）请简述参数估计中矩估计法的基本思想。",
        "用样本矩估计总体矩，从而得到参数的估计量。",
        "矩估计法：令样本原点矩等于总体原点矩，解方程得参数估计。"
    ))
    questions.append(Question(
        "P132-1", "P132", "统计概念",
        "（根据图片）请简述假设检验的基本步骤。",
        "1. 提出原假设和备择假设；2. 选择检验统计量；3. 给定显著性水平；4. 确定拒绝域；5. 计算统计量值并作出决策。",
        "假设检验的标准流程。"
    ))

    return questions

# ==================== 状态管理 ====================
class AppState:
    def __init__(self):
        self.questions = build_question_bank()
        self.current_index = 0
        self.total = len(self.questions)

    def get_current_question(self):
        return self.questions[self.current_index]

    def next_question(self):
        if self.current_index < self.total - 1:
            self.current_index += 1
            return True
        return False

    def prev_question(self):
        if self.current_index > 0:
            self.current_index -= 1
            return True
        return False

    def mark_done(self):
        self.get_current_question().is_done = True

    def random_question(self):
        self.current_index = random.randint(0, self.total - 1)

    def completed_count(self):
        return sum(1 for q in self.questions if q.is_done)

# ==================== UI 组件（同前，略作调整） ====================
def quiz_view(page: ft.Page, state: AppState):
    q = state.get_current_question()

    progress = ft.Row([
        ft.Text(f"第 {state.current_index+1} / {state.total} 题", size=16),
        ft.Text(f"已完成: {state.completed_count()}", size=14, color=ft.colors.GREY_600),
    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    question_text = ft.Text(q.question, size=20, weight=ft.FontWeight.BOLD, selectable=True)

    options_ui = None
    if q.options:
        options_ui = ft.Column([ft.Text(opt, size=16) for opt in q.options], spacing=5)

    answer_content = ft.Column(
        [
            ft.Divider(height=10),
            ft.Text(f"答案：{q.answer}", color=ft.colors.GREEN, weight=ft.FontWeight.BOLD),
            ft.Text(f"解析：\n{q.solution}", color=ft.colors.BLUE_400, selectable=True),
        ],
        visible=False,
        spacing=10
    )

    def toggle_answer(e):
        answer_content.visible = not answer_content.visible
        page.update()

    def go_prev(e):
        if state.prev_question():
            page.views[-1].controls[1] = quiz_view(page, state)
            page.update()

    def go_next(e):
        state.mark_done()
        if state.next_question():
            page.views[-1].controls[1] = quiz_view(page, state)
            page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("🎉 恭喜！已刷完所有题目！"), open=True)
            page.update()

    actions = ft.Row(
        [
            ft.ElevatedButton("上一题", on_click=go_prev, disabled=(state.current_index == 0)),
            ft.ElevatedButton("显示解析", on_click=toggle_answer),
            ft.ElevatedButton("下一题", on_click=go_next, disabled=(state.current_index == state.total-1)),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
    )

    return ft.Column(
        [
            progress,
            ft.Divider(height=10),
            question_text,
            options_ui if options_ui else ft.Container(),
            answer_content,
            ft.Divider(height=20),
            actions,
        ],
        scroll=ft.ScrollMode.AUTO,
        spacing=15,
        expand=True,
    )

def stats_view(page: ft.Page, state: AppState):
    total = state.total
    done = state.completed_count()
    percent = done / total * 100 if total > 0 else 0
    return ft.Column([
        ft.Text("📊 学习统计", size=24, weight=ft.FontWeight.BOLD),
        ft.Text(f"总题数：{total}", size=18),
        ft.Text(f"已完成：{done}", size=18),
        ft.Text(f"完成率：{percent:.1f}%", size=18),
        ft.ProgressBar(value=done/total if total>0 else 0, width=300),
        ft.Container(height=20),
        ft.ElevatedButton("返回主页", on_click=lambda _: page.go("/")),
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15)

# ==================== 主应用 ====================
def main(page: ft.Page):
    page.title = "概率论刷题复习"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO
    state = AppState()

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.View(
                    "/",
                    [
                        ft.AppBar(title=ft.Text("📚 概率论刷题"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Container(height=20),
                        ft.Text(f"总题数：{state.total}  已完成：{state.completed_count()}", size=16),
                        ft.Container(height=20),
                        ft.ElevatedButton("顺序刷题", on_click=lambda _: page.go("/quiz"), width=200),
                        ft.ElevatedButton("随机抽题", on_click=lambda _: [state.random_question(), page.go("/quiz")], width=200),
                        ft.ElevatedButton("查看统计", on_click=lambda _: page.go("/stats"), width=200),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=15,
                )
            )
        elif page.route == "/quiz":
            page.views.append(
                ft.View(
                    "/quiz",
                    [
                        ft.AppBar(title=ft.Text("刷题中"), bgcolor=ft.colors.SURFACE_VARIANT, leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: page.go("/"))),
                        quiz_view(page, state),
                    ],
                    scroll=ft.ScrollMode.AUTO,
                )
            )
        elif page.route == "/stats":
            page.views.append(
                ft.View(
                    "/stats",
                    [
                        ft.AppBar(title=ft.Text("统计"), bgcolor=ft.colors.SURFACE_VARIANT, leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: page.go("/"))),
                        stats_view(page, state),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )
        page.update()

    page.on_route_change = route_change
    page.go("/")

if __name__ == "__main__":
    ft.app(target=main)
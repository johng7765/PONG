# game_functions.py                   #
# Created by: John Gawlik             #
# Campus ID: 889752424                #
# Due: September 29th, 2018           #
#######################################


import sys
import pygame
from time import sleep


def change_ball_x_direction(ai_settings):
    ai_settings.ball_x_direction *= -1


def change_ball_y_direction(ai_settings):
    ai_settings.ball_y_direction *= -1


def check_ball_horizontal_edges(ai_settings, screen, stats, sb, paddle_top, paddle_bottom, paddle_left, comp_paddle_top,
                                comp_paddle_right, comp_paddle_bottom, ball):
    if ball.check_user_horizontal_edge():
        edge_hit(ai_settings, screen, stats, sb, paddle_top, paddle_bottom, paddle_left, comp_paddle_top,
                 comp_paddle_right, comp_paddle_bottom, ball)
    elif ball.check_comp_horizontal_edge():
        level_up(ai_settings, screen, stats, sb, paddle_top, paddle_bottom, paddle_left, comp_paddle_top,
                 comp_paddle_right, comp_paddle_bottom, ball)


def check_ball_vertical_top_edge(ai_settings, screen, stats, sb, paddle_top, paddle_bottom, paddle_left,
                                 comp_paddle_top, comp_paddle_right, comp_paddle_bottom, ball):
    if ball.check_user_vertical_top_edge():
        edge_hit(ai_settings, screen, stats, sb, paddle_top, paddle_bottom, paddle_left, comp_paddle_top,
                 comp_paddle_right, comp_paddle_bottom, ball)
    elif ball.check_comp_vertical_top_edge():
        level_up(ai_settings, screen, stats, sb, paddle_top, paddle_bottom, paddle_left, comp_paddle_top,
                 comp_paddle_right, comp_paddle_bottom, ball)


def check_ball_vertical_bottom_edge(ai_settings, screen, stats, sb, paddle_top, paddle_bottom, paddle_left,
                                    comp_paddle_top, comp_paddle_right, comp_paddle_bottom, ball):
    if ball.check_user_vertical_bottom_edge():
        edge_hit(ai_settings, screen, stats, sb, paddle_top, paddle_bottom, paddle_left, comp_paddle_top,
                 comp_paddle_right, comp_paddle_bottom, ball)
    elif ball.check_comp_vertical_bottom_edge():
        level_up(ai_settings, screen, stats, sb, paddle_top, paddle_bottom, paddle_left, comp_paddle_top,
                 comp_paddle_right, comp_paddle_bottom, ball)


def check_events(ai_settings, stats, sb, play_button, paddle_top, paddle_bottom, paddle_left, comp_paddle_top,
                 comp_paddle_right, comp_paddle_bottom, ball):
    """Respond to key presses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, paddle_top, paddle_bottom, paddle_left)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, paddle_top, paddle_bottom, paddle_left)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, stats, sb, play_button, paddle_top, paddle_bottom, paddle_left,
                              comp_paddle_top, comp_paddle_right, comp_paddle_bottom, ball, mouse_x, mouse_y)


def check_keydown_events(event, paddle_top, paddle_bottom, paddle_left):
    """Respond to key presses."""
    if event.key == pygame.K_UP:
        # Move the right paddle up.
        paddle_left.moving_up = True
    elif event.key == pygame.K_DOWN:
        # Move the right paddle down.
        paddle_left.moving_down = True

    if event.key == pygame.K_RIGHT:
        # Move the bottom paddle right.
        paddle_top.moving_right = True
        paddle_bottom.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move the bottom paddle left.
        paddle_top.moving_left = True
        paddle_bottom.moving_left = True


def check_keyup_events(event, paddle_top, paddle_bottom, paddle_left):
    """Respond to key releases."""
    if event.key == pygame.K_UP:
        paddle_left.moving_up = False
    elif event.key == pygame.K_DOWN:
        paddle_left.moving_down = False

    if event.key == pygame.K_RIGHT:
        paddle_top.moving_right = False
        paddle_bottom.moving_right = False
    elif event.key == pygame.K_LEFT:
        paddle_top.moving_left = False
        paddle_bottom.moving_left = False


def check_play_button(ai_settings, stats, sb, play_button, paddle_top, paddle_bottom, paddle_left, comp_paddle_top,
                      comp_paddle_right, comp_paddle_bottom, ball, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        # Reset the game statistics
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images
        sb.prep_computer_score()
        sb.prep_player_score()

        # create new paddles and center them
        comp_paddle_top.center_comp_paddle_top()
        comp_paddle_right.center_comp_paddle_right()
        comp_paddle_bottom.center_comp_paddle_bottom()
        paddle_top.center_paddle_top()
        paddle_bottom.center_paddle_bottom()
        paddle_left.center_paddle_left()
        ball.center_ball()


def draw_text(text, font, screen, x, y):
    text_obj = font.render(text, 1, (255, 255, 255))
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_obj, text_rect)


def edge_hit(ai_settings, screen, stats, sb, paddle_top, paddle_bottom, paddle_left, comp_paddle_top, comp_paddle_right,
             comp_paddle_bottom, ball):
    if stats.computer_score < 14:
        # Increase computer_score.
        stats.computer_score += 1
        sb.prep_computer_score()

        # Update scoreboard.
        sb.prep_computer_score()

        ai_settings.ball_x_direction *= -1
        if stats.computer_score % 2 == 0:
            ai_settings.ball_y_direction = 1
        else:
            ai_settings.ball_y_direction = -1

        # create new paddles and center them
        comp_paddle_top.center_comp_paddle_top()
        comp_paddle_right.center_comp_paddle_right()
        comp_paddle_bottom.center_comp_paddle_bottom()
        paddle_top.center_paddle_top()
        paddle_bottom.center_paddle_bottom()
        paddle_left.center_paddle_left()
        ball.center_ball()

        # Pause.
        sleep(0.5)

    else:
        show_computer_wins(ai_settings, screen)
        sleep(5.0)
        stats.game_active = False
        pygame.mouse.set_visible(True)


def level_up(ai_settings, screen, stats, sb, paddle_top, paddle_bottom, paddle_left, comp_paddle_top, comp_paddle_right,
             comp_paddle_bottom, ball):
    if stats.player_score < 14:
        # Speed up the game
        ai_settings.increase_speed()

        # Increase player_score.
        stats.player_score += 1
        sb.prep_player_score()

        # Make Ball go away from player
        ai_settings.ball_x_direction *= -1
        if stats.player_score % 2 == 0:
            ai_settings.ball_y_direction = 1
        else:
            ai_settings.ball_y_direction = -1

        # create new paddles and center them
        comp_paddle_top.center_comp_paddle_top()
        comp_paddle_right.center_comp_paddle_right()
        comp_paddle_bottom.center_comp_paddle_bottom()
        paddle_top.center_paddle_top()
        paddle_bottom.center_paddle_bottom()
        paddle_left.center_paddle_left()
        ball.center_ball()

        # Pause.
        sleep(0.5)
    else:
        show_player_wins(ai_settings, screen)
        sleep(5.0)
        stats.game_active = False
        pygame.mouse.set_visible(True)


def show_computer_wins(ai_settings, screen):
    screen.fill(ai_settings.bg_color)
    font = pygame.font.SysFont('freesansbold.ttf', 200)
    draw_text('COMPUTER', font, screen, (ai_settings.screen_width / 2), ((ai_settings.screen_height / 2) - 100))
    draw_text('WINS!', font, screen, (ai_settings.screen_width / 2), (ai_settings.screen_height / 2) + 100)
    pygame.display.update()


def show_player_wins(ai_settings, screen):
    screen.fill(ai_settings.bg_color)
    font = pygame.font.SysFont('freesansbold.ttf', 200)
    draw_text('PLAYER', font, screen, (ai_settings.screen_width / 2), ((ai_settings.screen_height / 2) - 100))
    draw_text('WINS!', font, screen, (ai_settings.screen_width / 2), (ai_settings.screen_height / 2) + 100)
    pygame.display.update()


def show_start_screen(ai_settings, screen, play_button):
    screen.fill(ai_settings.bg_color)
    pong_font = pygame.font.SysFont('freesansbold.ttf', 320)
    ai_font = pygame.font.SysFont('freesansbold.ttf', 150)
    notes_str = 'First to 15 points wins!'
    notes_font = pygame.font.SysFont('freesansbold.ttf', 100)
    draw_text('PONG', pong_font, screen, (ai_settings.screen_width / 2), (ai_settings.screen_height / 4))
    draw_text('AI -- NO WALLS', ai_font, screen, (ai_settings.screen_width / 2), ((ai_settings.screen_height / 2) - 50))
    draw_text(notes_str, notes_font, screen, (ai_settings.screen_width / 2), ((ai_settings.screen_height / 2) + 50))
    play_button.draw_button()
    pygame.display.update()


def update_ball(ai_settings, screen, stats, sb, paddle_top, paddle_bottom, paddle_left, comp_paddle_top,
                comp_paddle_right, comp_paddle_bottom, ball, user_paddle_hit_sound, comp_paddle_hit_sound):
    """Check if the ball is at an edge, and then Update the position of the ball in the fleet."""
    check_ball_horizontal_edges(ai_settings, screen, stats, sb, paddle_top, paddle_bottom, paddle_left, comp_paddle_top,
                                comp_paddle_right, comp_paddle_bottom, ball)
    check_ball_vertical_top_edge(ai_settings, screen, stats, sb, paddle_top, paddle_bottom, paddle_left,
                                 comp_paddle_top, comp_paddle_right, comp_paddle_bottom, ball)
    check_ball_vertical_bottom_edge(ai_settings, screen, stats, sb, paddle_top, paddle_bottom, paddle_left,
                                    comp_paddle_top, comp_paddle_right, comp_paddle_bottom, ball)
    ball.update()

    # Look for Paddle-Ball collisions
    if pygame.sprite.collide_rect(comp_paddle_top, ball):
        comp_paddle_hit_sound.play()
        change_ball_y_direction(ai_settings)
    if pygame.sprite.collide_rect(comp_paddle_right, ball):
        comp_paddle_hit_sound.play()
        change_ball_x_direction(ai_settings)
    if pygame.sprite.collide_rect(comp_paddle_bottom, ball):
        comp_paddle_hit_sound.play()
        change_ball_y_direction(ai_settings)
    if pygame.sprite.collide_rect(paddle_top, ball):
        user_paddle_hit_sound.play()
        change_ball_y_direction(ai_settings)
    if pygame.sprite.collide_rect(paddle_left, ball):
        user_paddle_hit_sound.play()
        change_ball_x_direction(ai_settings)
    if pygame.sprite.collide_rect(paddle_bottom, ball):
        user_paddle_hit_sound.play()
        change_ball_y_direction(ai_settings)


def update_comp_paddle_top(comp_paddle_top, ball):
    """Check if the comp_paddle_top is at an edge, and then Update the position of the paddle."""
    if comp_paddle_top.check_right_edge() and ball.x >= comp_paddle_top.x:
        comp_paddle_top.update_right()
    if comp_paddle_top.check_left_edge() and ball.x <= comp_paddle_top.x:
        comp_paddle_top.update_left()


def update_comp_paddle_right(comp_paddle_right, ball):
    """Check if the comp_paddle_top is at an edge, and then Update the position of the paddle."""
    if comp_paddle_right.check_top_edge() and ball.y <= comp_paddle_right.y:
        comp_paddle_right.update_up()
    if comp_paddle_right.check_bottom_edge() and ball.y >= comp_paddle_right.y:
            comp_paddle_right.update_down()


def update_comp_paddle_bottom(comp_paddle_bottom, ball):
    """Check if the comp_paddle_bottom is at an edge, and then Update the position of the paddle."""
    if comp_paddle_bottom.check_right_edge() and ball.x >= comp_paddle_bottom.x:
        comp_paddle_bottom.update_right()
    if comp_paddle_bottom.check_left_edge() and ball.x <= comp_paddle_bottom.x:
        comp_paddle_bottom.update_left()


def update_user_paddle_top(paddle_top):
    """Check if the paddle_top is at an edge, and then Update the position of the paddle."""
    paddle_top.update()


def update_user_paddle_left(paddle_left):
    """Check if the paddle_left is at an edge, and then Update the position of the paddle."""
    paddle_left.update()


def update_user_paddle_bottom(paddle_bottom):
    """Check if the paddle_bottom is at an edge, and then Update the position of the paddle."""
    paddle_bottom.update()


def update_screen(ai_settings, screen, stats, sb, paddle_top, paddle_bottom, paddle_left, comp_paddle_top,
                  comp_paddle_right, comp_paddle_bottom, ball, play_button, net):
    """Update images on the screen and flip to a new screen."""
    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    net.blitme()
    paddle_top.blitme()
    paddle_bottom.blitme()
    paddle_left.blitme()
    comp_paddle_top.blitme()
    comp_paddle_right.blitme()
    comp_paddle_bottom.blitme()
    ball.blitme()

    # Draw the score information
    sb.show_scores()

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        show_start_screen(ai_settings, screen, play_button)

    # Make the most recently drawn screen visible
    pygame.display.flip()
